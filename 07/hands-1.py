from collections import defaultdict
from functools import cmp_to_key

with open('./input.txt', 'r') as f:
    lines = f.readlines()
    hand_bets = {line.split()[0]: int(line.split()[1].strip()) for line in lines}

def type_rank(hand):
    ''' Returns the type of a hand, which is a Type. '''
    labels = defaultdict(int)

    for label in hand:
        labels[label] += 1

    shape = sorted(list(labels.values()))

    if shape == [5]:
        return 7
    elif shape == [1, 4]:
        return 6
    elif shape == [2, 3]:
        return 5
    elif shape == [1, 1, 3]:
        return 4
    elif shape == [1, 2, 2]:
        return 3
    elif shape == [1, 1, 1, 2]:
        return 2
    else:
        return 1

def cmp(a, b):
    ''' Compare two hands. Returns -1 if first is weaker, 1 if second is weaker, 0 if equal. '''

    label_ranks = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
    }


    value_a = [type_rank(a)] + [label_ranks[card] for card in a]
    value_b = [type_rank(b)] + [label_ranks[card] for card in b]

    return (value_a > value_b) - (value_a < value_b)

sorted_hands = sorted(hand_bets, key=cmp_to_key(cmp))

winnings = sum(rank * hand_bets[hand] for rank, hand in enumerate(sorted_hands, start=1))
print(f'{winnings=}')
