import re
from functools import cache

with open('./input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

@cache
def poss(condition: str, springs: tuple) -> int:
    """Given a string of '.#?" and a tuple of broken springs, returns number of possible arrangements."""
    if len(springs) == 1:
        # the base case: one spring, one string
        spring_length = springs[0]
        if '#' in condition:
            known_parts = condition.strip('.?')
            if '.' in known_parts or len(known_parts) > spring_length:
                # an impossiblity
                res = 0
            else:
                margin = spring_length - len(known_parts)
                window_pattern = rf'(\?{{0,{margin}}}{re.escape(known_parts)}\?{{0,{margin}}})'
                window_match = re.search(window_pattern, condition)
                assert window_match is not None, f'{window_pattern} in {condition}'

                window = window_match.group(1)

                res = max(len(window) - spring_length + 1, 0)
        elif '.' in condition:
            res = sum(poss(c, springs) for c in condition.split('.'))
        else:
            # only ?s
            res = max(len(condition) - spring_length + 1, 0)
    else:
        # figure out where the first spring could be, then DP our way to victory
        if sum(springs) + len(springs) - 1 > len(condition):
            res = 0

        first, *rest = springs
        new_condition = condition.lstrip('.')
        if '#' in condition:
            known_start = new_condition.index('#')
            start_locations = list(range(known_start + 1))
        else:
            known_start = len(new_condition) - sum(springs) + len(springs) - 1
            start_locations = list(range(known_start))
        count = 0
        for i in start_locations:
            if i + first >= len(new_condition):
                break
            prefix = new_condition[i:i + first]
            buffer = new_condition[i + first]
            suffix = new_condition[i + first + 1:]
            if '.' not in prefix and buffer != '#':
                p = poss(suffix, tuple(rest))
                count += p

        res = count

    return res

def arrangements(line):
    condition, spring_record = line.split()
    springs = [int(s) for s in spring_record.split(',')]

    return poss("?".join([condition] * 5), tuple(springs * 5))

print(sum(arrangements(line) for line in lines))
