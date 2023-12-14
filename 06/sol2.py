def distances(total):
    return [(total - held) * held for held in range(total)]


print(len([d for d in distances(52947594) if d > 426137412791216]))
