file = open('./input.txt', 'r')
lines = file.readlines()
file.close();

def points(line):
    numbers = line.strip().split(':')[-1]
    winning, owned = numbers.split('|')

    winning = set(winning.strip().split())
    owned = set(owned.strip().split())

    matches = len(winning & owned)
    return 2 ** (matches - 1) if matches else 0

print(sum(points(line) for line in lines))
