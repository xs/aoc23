def distances(total):
    return [(total - held) * held for held in range(total)]

print(len([d for d in distances(52) if d > 426]))
print(len([d for d in distances(94) if d > 1374]))
print(len([d for d in distances(75) if d > 1279]))
print(len([d for d in distances(94) if d > 1216]))

print(31 * 57 * 22 * 63)
