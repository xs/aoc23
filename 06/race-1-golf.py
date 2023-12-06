def ways(total, record):
    distances = [(total - held) * held for held in range(total)]
    return len([d for d in distances if d > record])

print(ways(52, 426) * ways(94, 1374) * ways(75, 1279) * ways(94, 1216))
