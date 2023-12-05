import sys

lines = sys.stdin.readlines()

sum = 0

def calibrate(line):
    start = 0
    end = 0

    for char in line:
        if char.isdigit():
            start = int(char)
            break

    for char in reversed(line):
        if char.isdigit():
            end = int(char)
            break

    return 10 * start + end

for line in lines:
    sum += calibrate(line)

print(f'calibration sum: {sum}')

