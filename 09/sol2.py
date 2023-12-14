from itertools import pairwise

with open('./input.txt', 'r') as f:
    sequences = ([int(i) for i in line.split()] for line in f.readlines())

def prev_value(sequence):
    sequences = [sequence]

    while any(sequences[-1]):
        diffs = [b - a for a, b in pairwise(sequences[-1])]
        sequences.append(diffs)

    return sum((-1) ** i * sequence[0] for i, sequence in enumerate(sequences))

print(f'answer: {sum(prev_value(sequence) for sequence in sequences)}')
