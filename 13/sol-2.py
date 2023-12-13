from sys import stdin
from typing import List
from collections import defaultdict

patterns = [pattern_string.splitlines() for pattern_string in stdin.read().split("\n\n")]

def can_reflect(line: str, i: int) -> bool:
    """Given a line and index, returns True if the string reflects at that index"""
    normal = reversed(line[:i])
    reflection = line[i:]
    return all(p == q for p, q in zip(normal, reflection))

def get_reflections(line: str):
    """Given a line, return columns before which a line of reflection may exist."""
    return set(i for i in range(1, len(line)) if can_reflect(line, i))

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
