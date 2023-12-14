from sys import stdin
from typing import List
from collections import defaultdict, Counter

patterns = [pattern_string.splitlines() for pattern_string in stdin.read().split("\n\n")]

def can_reflect(line: str, i: int) -> bool:
    """Given a line and index, returns True if the string reflects at that index"""
    return all(p == q for p, q in zip(reversed(line[:i]), line[i:]))

def get_reflections(line: str):
    """Given a line, return columns before which a line of reflection may exist."""
    return set(i for i in range(1, len(line)) if can_reflect(line, i))

def vertical_candidates(pattern: List[str]) -> List[int]:
    """Return possible candidates for a new post-smudge vertical reflection line."""
    reflections = Counter()
    for line in pattern:
        reflections += Counter(get_reflections(line))

    return [r for r in reflections if reflections[r] == len(pattern) - 1]

def horizontal_candidates(pattern: List[str]) -> List[int]:
    """Return possible candidates for a new post-smudge horizontal reflection line."""
    reflections = Counter()
    for line in zip(*pattern):
        reflections += Counter(get_reflections(line))

    return [r for r in reflections if reflections[r] == len(pattern[0]) - 1]

def value(pattern):
    # NOTE: this only works because each pattern in the input has a unique new reflection candidate
    # I tested by printing len(v + h) for all patterns and saw the output [1, 1, 1, ... 1]
    v = vertical_candidates(pattern)
    h = horizontal_candidates(pattern)
    return v[0] if v else 100 * h[0]

print(sum(value(p) for p in patterns))
