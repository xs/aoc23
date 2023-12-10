with open('input.txt', 'r') as f:
    lines = f.readlines()

def calibrate(line):
    start = int(next(char for char in line if char.isdigit()))
    end = int(next(char for char in reversed(line) if char.isdigit()))

    return 10 * start + end

print(f'calibration sum: {sum(calibrate(line) for line in lines)}')
