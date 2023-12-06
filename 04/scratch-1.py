import re

file = open('./input.txt', 'r')
lines = file.readlines()
file.close();

points = 0

for line in lines:
    print(f'testing... {line}')
    numbers = line.strip().split(':')[-1]
    winning, owned = numbers.split('|')

    winning = set(winning.strip().split())
    owned = set(owned.strip().split())

    matches = winning & owned

    if matches:
        print(f'matches! {matches}')
        points += 2 ** (len(matches) - 1)

print(f'total points: {points}')

