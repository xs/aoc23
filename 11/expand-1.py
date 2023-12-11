from itertools import combinations

with open('./input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

transpose = []

for col in zip(*lines):
    transpose.append(col)
    if '#' not in col:
        transpose.append(col)

grid = []
for row in zip(*transpose):
    grid.append(row)
    if '#' not in row:
        grid.append(row)

galaxies = []

for r, row in enumerate(grid):
    for c, tile in enumerate(row):
        if tile == '#':
            galaxies.append((r, c))

galaxy_pairs = list(combinations(galaxies, 2))

def dist(a, b):
    x_a, y_a = a
    x_b, y_b = b
    return abs(x_a - x_b) + abs(y_a - y_b)

print(f'answer: {sum(dist(*pair) for pair in galaxy_pairs)}')
