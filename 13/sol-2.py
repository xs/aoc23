from sys import stdin
from typing import List
from collections import defaultdict

lines = [line.strip() for line in stdin.readlines()] + [""]
patterns = []

while lines:
    next_empty = lines.index("")
    patterns.append(lines[:next_empty])
    lines.pop(next_empty)
    del lines[:next_empty]

def get_reflections(line: str):
    """Given a line, return columns before which a line of reflection may exist."""

    indices = set()
    for i in range(1, len(line)):
        normal = reversed(line[:i])
        reflection = line[i:]
        if all(p == q for p, q in zip(normal, reflection)):
            indices.add(i)

    return indices

def vertical_candidates(pattern: List[str]) -> List[int]:
    """Return possible candidates for a new post-smudge vertical reflection line."""
    reflections = defaultdict(int)
    for line in pattern:
        for reflection in get_reflections(line):
            reflections[reflection] += 1

    return [r for r in reflections if reflections[r] == len(pattern) - 1]


def horizontal_candidates(pattern: List[str]) -> List[int]:
    """Return possible candidates for a new post-smudge horizontal reflection line."""
    reflections = defaultdict(int)
    for line in zip(*pattern):
        for reflection in get_reflections(line):
            reflections[reflection] += 1

    return [r for r in reflections if reflections[r] == len(pattern[0]) - 1]

def value(pattern):
    # NOTE: this only works because each pattern in the input has a unique new reflection candidate
    # I tested by printing len(v + h) for all patterns and saw the output [1, 1, 1, ... 1]
    v = vertical_candidates(pattern)
    h = horizontal_candidates(pattern)
    if v:
        return v[0]
    else:
        return 100 * h[0]


print(sum(value(p) for p in patterns))
