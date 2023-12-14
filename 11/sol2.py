from itertools import combinations

with open('./input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

empty_cols = set()
empty_rows = set()

for c, col in enumerate(zip(*lines)):
    if '#' not in col:
        empty_cols.add(c)

for r, row in enumerate(lines):
    if '#' not in row:
        empty_rows.add(r)

galaxies = []

for r, row in enumerate(lines):
    for c, tile in enumerate(row):
        if tile == '#':
            galaxies.append((r, c))

galaxy_pairs = list(combinations(galaxies, 2))

def dist(a, b):
    r_a, c_a = a
    r_b, c_b = b
    rows = sorted([r_a, r_b])
    cols = sorted([c_a, c_b])
    empties = len(empty_rows & set(range(*rows))) + len(empty_cols & set(range(*cols)))
    return abs(r_a - r_b) + abs(c_a - c_b) + 999999 * empties

print(f'answer: {sum(dist(*pair) for pair in galaxy_pairs)}')
