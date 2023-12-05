import sys

lines = sys.stdin.readlines()

sum = 0

def power(line):
    _, cubesets = line.split(':')

    cubesets = cubesets.strip().split(';')

    print('\n power solving...')

    r = 0
    g = 0
    b = 0

    for cubeset in cubesets:
        cubegroups = cubeset.strip().split(',')
        for cubegroup in cubegroups:
            print(cubegroup.strip())

            number, color = cubegroup.strip().split()
            number = int(number)

            if color == 'red':
                r = max(number, r)
            elif color == 'green':
                g = max(number, g)
            elif color == 'blue':
                b = max(number, b)


    print(f'{r} red, {g} green, {b}, blue')

    return r * g * b


for line in lines:
    sum += power(line.strip())

print(f'power sum: {sum}')

