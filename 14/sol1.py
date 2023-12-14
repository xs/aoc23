from sys import stdin

lines = [line.strip() for line in stdin]

def load(col: str) -> int:
    """Given a column, tilt all O to the nearest # and and return total load"""
    tilted = []
    empty_space = 0

    for c in col:
        if c == 'O':
            tilted.append('O')
        elif c == '.':
            empty_space += 1
        elif c == '#':
            tilted += ['.'] * empty_space
            tilted.append('#')
            empty_space = 0
    tilted += ['.'] * empty_space

    return sum(i for i, tile in enumerate(reversed(tilted), start=1) if tile == 'O')

print(sum(load(col) for col in zip(*lines)))
