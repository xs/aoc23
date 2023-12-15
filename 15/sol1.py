from sys import stdin

seq = stdin.readline().strip().split(',')

def hash(chars):
    current_value = 0
    for char in chars:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

print(sum(hash(step) for step in seq))
