from sys import stdin
from typing import List

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

def vertical(pattern: List[str]) -> int | None:
    """Return the vertical reflection line or None if none exists."""
    reflections = set(range(1, len(pattern[0])))
    for line in pattern:
        reflections = reflections & get_reflections(line)
        if not reflections:
            return None
    return reflections.pop()

def horizontal(pattern: List[str]) -> int | None:
    """Return the horizontal reflection line or None if none exists."""
    reflections = set(range(1, len(pattern)))
    for line in zip(*pattern):
        reflections = reflections & get_reflections(line)
        if not reflections:
            return None
    return reflections.pop()

def value(pattern):
    v = vertical(pattern)
    if v:
        return v
    else:
        h = horizontal(pattern)
        assert h is not None
        return 100 * h


print(sum(value(p) for p in patterns))
