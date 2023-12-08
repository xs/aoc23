import re
from collections import defaultdict
from math import gcd, prod

def locations(line):
    return (m.group() for m in re.finditer(r'(\w+)', line))

with open('./input.txt', 'r') as f:
    path, _, *node_lines = f.readlines()
    path = path.strip()
    network = {start: {"L": left, "R": right} for start, left, right in map(locations, node_lines)}

def cycle(start, path, network):
    ''' Follows every turn in path; returns a tuple when the same node and path index
    is seen at the end of path cycle. '''

    # keys are [airport code, index into the LR path]
    seen = defaultdict(list)
    at = start
    step = 0

    while True:
        history = seen[(at, step % len(path))]
        history.append(step)
        if len(history) > 1:
            print(f'starting at {start}, we loop at {history}')
            return history
        else:
            turn = path[step % len(path)]
            at = network[at][turn]
            step += 1


def z_indices(start, path, network, end_criterion, cycle):
    ''' For the length of the cycle, return all indices which meet the end criterion. '''

    step = 0
    at = start
    results = []

    # fast forward
    for step in range(cycle[0]):
        turn = path[step]
        at = network[at][turn]

    for step in range(*cycle):
        turn = path[step % len(path)]
        at = network[at][turn]

        if end_criterion(at):
            results.append(step + 1)

    return results

start_criterion = lambda x: x.endswith('A')
end_criterion = lambda x: x.endswith('Z')

starts = filter(start_criterion, network)

cycles = {start: cycle(start, path, network) for start in starts}
z_sets = [z_indices(start, path, network, end_criterion, cycles[start]) for start in cycles]

print(cycles)
# => {'DPA': [3, 20780], 'QLA': [5, 19204], 'VJA': [4, 18677], 'GTA': [2, 16045], 'AAA': [4, 12365], 'XQA': [2, 15519]}

print(z_sets)
# => [[20777], [19199], [18673], [16043], [12361], [15517]]

print([gcd(z[0], len(path)) for z in z_sets])
# => [263, 263, 263, 263, 263, 263]

num_cycles = [z[0] / 263 for z in z_sets]
print(num_cycles)
# => [79.0, 73.0, 71.0, 61.0, 47.0, 59.0]
# cool look at all those prime numbers 🙄

print(int(prod(num_cycles)))
# => 69260879921
