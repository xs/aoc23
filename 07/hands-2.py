from collections import defaultdict

with open('./input.txt', 'r') as f:
    lines = f.readlines()
    hand_bets = {line.split()[0]: int(line.split()[1].strip()) for line in lines}

def type_rank(hand):
    labels = defaultdict(int)

    for label in hand:
        labels[label] += 1

    jokers = labels['J']
    del labels['J']

    shape = sorted(list(labels.values()), reverse=True) or [0]
    shape[0] += jokers

    type_ranks = [
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1],
        [2, 2, 1],
        [3, 1, 1],
        [3, 2],
        [4, 1],
        [5],
    ]

    return type_ranks.index(shape)

def hand_value(hand):
    return [type_rank(hand)] + ['J23456789TQKA'.index(card) for card in hand]

sorted_hands = sorted(hand_bets, key=hand_value)
winnings = sum(rank * hand_bets[hand] for rank, hand in enumerate(sorted_hands, start=1))

print(f'{winnings=}')
