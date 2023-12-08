import re
from itertools import product
from typing import Any, List

file = open('./input.txt', 'r')
lines = file.readlines()
file.close();

width = len(lines[0])
height = len(lines)

grid: List[List[Any]] = [[None for _ in range(width)] for _ in range(height)]

parts = []
gears = []

for row, line in enumerate(lines):
    part_matches = re.finditer(r'\d+', line.strip())

    for match in part_matches:
        part_id = len(parts)
        part = (int(match.group()), part_id)
        parts.append(part)

        for col in range(*match.span()):
            grid[row][col] = part

    symbol_matches = re.finditer(r'\*', line.strip())

    for match in symbol_matches:
        gear = (row, match.start())
        gears.append(gear)

def get(r, c):
    if r < 0 or c < 0 or r >= height or c >= height:
        return None

    return grid[r][c]

sum = 0

for gear in gears:
    r, c = gear

    coords = product([r - 1, r, r + 1], [c - 1, c, c + 1])

    adjacents = set(get(*coord) for coord in coords)
    adjacents.remove(None)

    if len(adjacents) == 2:
        print(f'gear! {adjacents}')

        adjacents = list(adjacents)
        first, second = adjacents

        assert first is not None
        assert second is not None

        power_ratio = first[0] * second[0]

        sum += power_ratio


print(f'power ratio sum: {sum}')

