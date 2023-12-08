import re

def locations(line):
    return (m.group() for m in re.finditer(r'(\w+)', line))

with open('./input.txt', 'r') as f:
    path, _, *node_lines = f.readlines()
    path = path.strip()
    network = {start: {"L": left, "R": right} for start, left, right in map(locations, node_lines)}

def traverse(start, end, path, network):
    turns = 0
    at = start

    while at != end:
        turn = path[turns % len(path)]
        at = network[at][turn]
        turns += 1

    print(f'{start} to {end} in {turns} turns')

traverse('AAA', 'ZZZ', path, network)
