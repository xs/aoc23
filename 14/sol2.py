from sys import stdin
from typing import Tuple

grid = tuple(tuple(c for c in line.strip()) for line in stdin)
Grid = Tuple[Tuple[str, ...], ...]

def load(col: tuple) -> int:
    """Given a tilted column, return total load"""
    return sum(i for i, tile in enumerate(reversed(col), start=1) if tile == 'O')

def tilt_left(row: tuple) -> tuple:
    """ Tilts a row leftward."""
    tilted = []
    empty_space = 0


    for c in row:
        if c == 'O':
            tilted.append('O')
        elif c == '.':
            empty_space += 1
        elif c == '#':
            tilted += ['.'] * empty_space
            tilted.append('#')
            empty_space = 0
    tilted += ['.'] * empty_space

    return tuple(tilted)

def tilt(grid: Grid) -> Grid:
    """Tilts the grid north. Transpose, tilt left, transpose."""
    return tuple(zip(*[tilt_left(col) for col in zip(*grid)]))

def rotate(grid: Grid) -> Grid:
    """Given a grid, rotate 90 degrees clockwise."""
    return tuple(tuple(reversed(row)) for row in zip(*grid))

def cycle(grid: Grid) -> Grid:
    """Perform a N W S E spin-cycle."""
    return rotate(tilt(rotate(tilt(rotate(tilt(rotate(tilt(grid))))))))

seen = {}
grids = []
total_cycles = 1000000000

for i in range(total_cycles):
    seen[grid] = i
    grids.append(grid)
    grid = cycle(grid)

    if grid in seen:
        first_seen = seen[grid]
        cycle_length = i - first_seen + 1

        final_index = (total_cycles - first_seen) % cycle_length + first_seen
        final_grid = grids[final_index]

        print(sum(load(col) for col in zip(*final_grid)))
        break
