with open('./input.txt', 'r') as file:
    lines = file.readlines()

def points(line):
    _, numbers = line.split(':')
    winning, owned = numbers.split('|')

    matches = set(winning.split()) & set(owned.split())
    return 2 ** (len(matches) - 1) if matches else 0

print(sum(points(line) for line in lines))
