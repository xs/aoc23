from collections import defaultdict

with open('./input.txt', 'r') as f:
    lines = f.readlines()

points = 0
copies = defaultdict(int)

def matches(line):
    _, numbers = line.split(':')
    winning, owned = numbers.split('|')

    return len(set(winning.split()) & set(owned.split()))

for line in reversed(lines):
    card_number = int(line.split(':')[0].split()[-1])

    new_copies = 1
    prizes = range(card_number + 1, card_number + matches(line) + 1)

    for prize in prizes:
        new_copies += copies[prize]

    copies[card_number] = new_copies
    points += new_copies

print(f'total points: {points}')
