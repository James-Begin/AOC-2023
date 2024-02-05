times = [61,67,75,71]
dists = [430,1036,1307,1150]

time = int(''.join(str(_) for _ in times))
dist = int(''.join(str(_) for _ in dists))

ans = 0
for i in range(time):
    if (time-i) * (i) > dist:
        ans += 1
print((ans))
