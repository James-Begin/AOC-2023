from math import prod

times = [61,67,75,71]
dists = [430,1036,1307,1150]

ans = [0]*4

for k,v in enumerate(times):
    for i in range(v):
        if (v-i) * (i) > dists[k]:
            ans[k] += 1
print(prod(ans))
