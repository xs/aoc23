import sys

lines = sys.stdin.readlines()

sum = 0

def score(line):
    game, cubesets = line.split(':')

    game_id = int(game.split()[-1])

    cubesets = cubesets.strip().split(';')

    for cubeset in cubesets:
        cubegroups = cubeset.strip().split(',')
        print('\ntesting...')
        for cubegroup in cubegroups:
            print(cubegroup)

            number, color = cubegroup.strip().split()

            if color == 'red' and int(number) > 12:
                print('unsolvable')
                return 0
            elif color == 'green' and int(number) > 13:
                print('unsolvable')
                return 0
            elif color == 'blue' and int(number) > 14:
                print('unsolvable')
                return 0

        print('solvable!')
    return game_id


for line in lines:
    sum += score(line.strip())

print(f'solvable game sum: {sum}')

