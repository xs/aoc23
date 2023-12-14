from collections import defaultdict
import re

with open('./input.txt', 'r') as f:
    seed_line, _, *lines = f.readlines()
    _, *seeds = seed_line.split()

# key: e.g. seed-to-soil, value: sorted list of (source, length, dest) tuples
maps = defaultdict(list)

current_map = None

RE_MAP = r'([\w-]+) map:'
RE_RANGES = r'\d+ \d+ \d+'

# preprocess maps

for line in lines:
    map_match = re.match(RE_MAP, line)
    range_match = re.match(RE_RANGES, line)
    if map_match:
        if current_map:
            maps[current_map].sort()
        current_map = map_match.group(1)

    elif range_match:
        dest_start, source_start, length = map(int, line.split())

        maps[current_map].append((source_start, length, dest_start))

maps[current_map].sort()

def transform(map_name, source):
    tuples = maps[map_name]

    for source_start, length, dest_start in tuples:
        if source < source_start:
            return source
        elif source < source_start + length:
            return source - source_start + dest_start
        else:
            continue

    return source

def location(seed):
    soil = transform('seed-to-soil', seed)
    fertilizer = transform('soil-to-fertilizer', soil)
    water = transform('fertilizer-to-water', fertilizer)
    light = transform('water-to-light', water)
    temperature = transform('light-to-temperature', light)
    humidity = transform('temperature-to-humidity', temperature)
    return transform('humidity-to-location', humidity)

print(min(location(int(seed)) for seed in seeds))

