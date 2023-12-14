from itertools import product

with open('./input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

def count_springs(condition):
    return [len(spring) for spring in condition.split('.') if spring]


def arrangements(line):
    condition_record, spring_record = line.split()
    springs = [int(s) for s in spring_record.split(',')]

    unknowns = condition_record.count('?')

    replacements = product(*['#.'] * unknowns)

    count = 0
    for replacement in replacements:
        test_condition = condition_record
        for r in replacement:
            test_condition = test_condition.replace('?', r, 1)

        if count_springs(test_condition) == springs:
            count += 1

    return count

print(sum(arrangements(line) for line in lines))
