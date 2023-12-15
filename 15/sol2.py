from collections import defaultdict
import re
from sys import stdin

seq = stdin.readline().strip().split(',')

def hash(chars):
    current_value = 0
    for char in chars:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

boxes = defaultdict(dict)

for step in seq:
    match = re.search(r'^(\w+)(-|=\d+)$', step)
    assert match

    label, op = match.groups()

    box = boxes[hash(label)]

    if op.startswith('='):
        focal_length = int(op[1:])
        box[label] = focal_length
    else:
        if label in box:
            del box[label]

def score_box(box, box_number):
    return (box_number + 1) * sum(slot * box[label] for slot, label in enumerate(box, start=1))

print(sum(score_box(box, box_number) for box_number, box in boxes.items()))
