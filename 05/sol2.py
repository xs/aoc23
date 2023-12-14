from collections import defaultdict
import re
import time

start_time = time.time()
print(f'starting at {start_time}')

with open('./input.txt', 'r') as f:
    seed_line, _, *lines = f.readlines()
    _, *seeds = seed_line.split()

# key: e.g. seed-to-soil, value: sorted list of (source, length, dest) tuples
dest_maps = defaultdict(list)

current_map = None

RE_MAP = r'([\w-]+) map:'
RE_RANGES = r'\d+ \d+ \d+'

for line in lines:
    map_match = re.match(RE_MAP, line)
    range_match = re.match(RE_RANGES, line)
    if map_match:
        if current_map:
            dest_maps[current_map].sort()
        current_map = map_match.group(1)

    elif range_match:
        dest_start, source_start, length = map(int, line.split())

        dest_maps[current_map].append((dest_start, length, source_start))

dest_maps[current_map].sort()

def transform_to_source(map_name, dest):
    for dest_start, length, source_start in dest_maps[map_name]:
        if dest < dest_start:
            return dest
        elif dest < dest_start + length:
            return dest - dest_start + source_start
        else:
            continue

    return dest


def seed(location):
    humidity = transform_to_source('humidity-to-location', location)
    temperature = transform_to_source('temperature-to-humidity', humidity)
    light = transform_to_source('light-to-temperature', temperature)
    water = transform_to_source('water-to-light', light)
    fertilizer = transform_to_source('fertilizer-to-water', water)
    soil = transform_to_source('soil-to-fertilizer', fertilizer)
    return transform_to_source('seed-to-soil', soil)


# process seed ranges line

running = True
seeds = iter(seeds)
seed_ranges = []

while running:
    try:
        seed_ranges.append((int(next(seeds)), int(next(seeds))))
    except StopIteration:
        running = False

seed_ranges.sort()

# here we go. brute force every location starting at 0

min_location = 0

while True:
    s = seed(min_location)

    for seed_start, length in seed_ranges:
        if s < seed_start:
            break
        elif s < seed_start + length:
            end_time = time.time()
            print(f'done: seed {s} for location {min_location}')
            print(f'took: {end_time - start_time} seconds')
            exit()
        else:
            continue

    min_location += 1

