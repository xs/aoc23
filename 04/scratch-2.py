from collections import defaultdict
import re

file = open('./input.txt', 'r')
lines = file.readlines()
file.close();

points = 0

copies = defaultdict(int)

def matches(line):
    numbers = line.strip().split(':')[-1]
    winning, owned = numbers.split('|')

    winning = set(winning.strip().split())
    owned = set(owned.strip().split())

    return len(winning & owned)


for line in reversed(lines):
    card_number = int(line.split(':')[0].split()[-1])

    new_copies = 1
    prizes = range(card_number + 1, card_number + matches(line) + 1)

    for prize in prizes:
        new_copies += copies[prize]

    copies[card_number] = new_copies
    points += new_copies

print(f'total points: {points}')
