with open('inp.txt') as f:
    file = f.read().split("\n\n")

ranges = [lines.split("\n") for lines in file]

seeds = [int(seed) for seed in ranges[0][0].split()[1:]]

mapping = [[(source, source + num, destination - source)  # Map to start, stop, offset
        for destination, source, num in [[int(n) for n in line.split()]
        for line in lines[1:]]]
        for lines in ranges[1:]]

seeds = [(seed, seed+1) for seed in seeds]

def updaterange(start, stop, mapping):

    if stop <= start:
        return []

    for begin, end, diff in mapping:
        if begin <= start < end and begin < stop <= end:
            return [(start + diff, stop + diff)]

        if stop <= begin or start >= end:
            continue

        return (updaterange(start, begin, mapping) + [(max(start, begin) + diff, min(stop, end) + diff)]
            + updaterange(end, stop, mapping))

    return [(start, stop)]

for map in mapping:
    seeds = [new_seed for seed, num in seeds for new_seed in updaterange(seed, num, map)]

print(min(seeds)[0])


