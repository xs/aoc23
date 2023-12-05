import sys
import re

lines = sys.stdin.readlines()

sum = 0

digit_pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
digit_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        }

def num(digit):
    if digit in digit_map:
        return digit_map[digit]
    else:
        return int(digit)

def calibrate(line):
    print(f'calibrating {line}')
    digits = re.findall(digit_pattern, line)

    print(f'digits: {digits}')

    value = 10 * num(digits[0]) + num(digits[-1])
    print(f'value: {value}\n')
    return value

for line in lines:
    sum += calibrate(line.strip())

print(f'calibration sum: {sum}')

