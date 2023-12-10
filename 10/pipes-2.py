import re
from itertools import product
from typing import Iterable, Tuple, List, TypeVar

T = TypeVar('T')
Grid = List[List[T]]
Coord = Tuple[int, int]
Pipe = List[Coord]

PIPES = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    'L': [(-1, 0), (0, 1)],
    '7': [(0, -1), (1, 0)],
    'F': [(0, 1), (1, 0)],
    '.': [],
    'S': [],
    None: [],
}

REVERSE_PIPE_MAP = {
    ((-1, 0), (1, 0)): '|',
    ((-1, 0), (0, -1)): 'J',
    ((-1, 0), (0, 1)): 'L',
    ((0, -1), (0, 1)): '-',
    ((0, -1), (1, 0)): '7',
    ((0, 1), (1, 0)): 'F',
}


class Field(object):
    def __init__(self, grid: List[List[str]]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

        self.start = (0, 0)

        for r, row in enumerate(grid):
            for c, tile in enumerate(row):
                if tile == 'S':
                    self.start = (r, c)
                    self.replace_start_pipe()
                    break

        self.path = set()
        self.landscaped = False


    def replace_start_pipe(self):
        ''' Replaces the 'S' tile with an appropriate pipe tile. '''
        connections = []
        for neighbor in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            try:
                neighbor_pipe = PIPES[self.peek(self.start, neighbor)]
                self.through(neighbor, neighbor_pipe)
                connections.append(neighbor)
            except:
                continue

        r, c = self.start
        start_pipe: Tuple[Coord, Coord] = (connections[0], connections[1])

        self.grid[r][c] = REVERSE_PIPE_MAP[start_pipe]

    def all_coords(self) -> Iterable[Coord]:
        ''' Returns an iterator of all (r, c) tuples '''
        return product(range(self.height), range(self.width))


    def move(self, start: Coord, offset: Coord) -> Coord:
        ''' Given an absolute start and relative offset, returns the new absolute (r, c) '''
        return (start[0] + offset[0], start[1] + offset[1])

    def peek(self, start: Coord, offset: Coord) -> str | None:
        ''' Returns tile at an offset; None if out of bounds '''
        r, c = self.move(start, offset)
        if r < 0 or c < 0 or r >= self.height or c >= self.height:
            return None

        return self.grid[r][c]

    def through(self, offset: Coord, pipe: Pipe) -> Coord:
        ''' Attempt stepping through pipe.

        Raises ValueError if not possible; otherwise returns a new offset for next move.
        '''
        from_offset = (-offset[0], -offset[1])

        from_index = pipe.index(from_offset)
        return pipe[(from_index + 1) % 2]

    def traverse(self) -> None:
        ''' Traverses pipe loop starting at self.start. '''
        self.path.add(self.start)
        at = self.start
        next_coord = self.start
        next_offset = (0, 0)

        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tile = self.peek(at, neighbor)
            if tile and PIPES[tile]:
                next_coord = self.move(at, neighbor)
                try:
                    next_offset = self.through(neighbor, PIPES[tile])
                except ValueError:
                    continue

        at = next_coord

        while at != self.start:
            self.path.add(at)
            next_tile = self.peek(at, next_offset)
            at = self.move(at, next_offset)
            next_offset = self.through(next_offset, PIPES[next_tile])


    def landscape(self) -> None:
        ''' Clear all pipe not on the path.

        Traverses field first if not already traversed. '''

        if not self.path:
            self.traverse()

        for r, c in self.all_coords():
            if (r, c) not in self.path:
                self.grid[r][c] = '.'

        self.landscaped = True

    def is_enclosed(self, coord: Coord) -> bool:
        ''' Returns True if coord is enclosed; False if not.

        Landscapes (and traverses) field first if not already landscaped. '''

        if not self.landscaped:
            self.landscape()

        if coord in self.path:
            return False
        else:
            r, c = coord
            escape_route = ''.join(self.grid[r][:c])
            crossings = list(re.finditer(r'(\||L-*7|F-*J)', escape_route))
            return len(crossings) % 2 == 1

    def count_enclosed_tiles(self) -> int:
        ''' Counts enclosed tiles. '''
        return sum(self.is_enclosed(coord) for coord in self.all_coords())


with open('./input.txt', 'r') as f:
    grid: Grid[str] = [[char for char in line.strip()] for line in f.readlines()]
    field = Field(grid)
    field.traverse()
    field.landscape()

    print(f'enclosed tiles: {field.count_enclosed_tiles()}')

