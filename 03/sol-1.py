import re

file = open('./input.txt', 'r')
lines = file.readlines()
file.close();

# list of (number, row, start_col, end_col) tuples
parts = list()

# set of (row, col) tuples
symbols = set()

for row, line in enumerate(lines):
    part_matches = re.finditer(r'\d+', line.strip())

    for match in part_matches:
        part = (int(match.group()), row, match.start(), match.end())
        parts.append(part)

    symbol_matches = re.finditer(r'[^\d\.]', line.strip())

    for match in symbol_matches:
        symbol = (row, match.start())
        symbols.add(symbol)


sum = 0

for part in parts:
    number, row, start, end = part

    above = [(row - 1, col) for col in range(start - 1, end + 1)]
    sides = [(row, start - 1), (row, end)]
    below = [(row + 1, col) for col in range(start - 1, end + 1)]

    coords = set(above + sides + below)

    if coords & symbols:
        sum += number
        print(f'{number} included, sum now {sum}!')


print(f'solvable game sum: {sum}')

