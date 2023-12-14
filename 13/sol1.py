from sys import stdin
from typing import List

patterns = [pattern_string.splitlines() for pattern_string in stdin.read().split("\n\n")]

def can_reflect(line: str, i: int) -> bool:
    """Given a line and index, returns True if the string reflects at that index"""
    return all(p == q for p, q in zip(reversed(line[:i]), line[i:]))

def get_reflections(line: str):
    """Given a line, return columns before which a line of reflection may exist."""
    return set(i for i in range(1, len(line)) if can_reflect(line, i))

def vertical(pattern: List[str]) -> int | None:
    """Return the vertical reflection line or None if none exists."""
    reflections = set(range(1, len(pattern[0])))
    for line in pattern:
        reflections &= get_reflections(line)
    return reflections.pop() if reflections else None

def horizontal(pattern: List[str]) -> int | None:
    """Return the horizontal reflection line or None if none exists."""
    reflections = set(range(1, len(pattern)))
    for line in zip(*pattern):
        reflections &= get_reflections(line)
    return reflections.pop() if reflections else None

def value(pattern):
    v = vertical(pattern) or 0
    h = horizontal(pattern) or 0
    return 100 * h + v

print(sum(value(p) for p in patterns))
