from collections import defaultdict
import re

with open('inp.txt') as f:
    file = f.read().splitlines()

commands = file.pop(0)

del file[0]
start = 'AAA'
store = defaultdict()

for line in file:
    line = re.split('[( , )]', line)
    store[line[0]] = [line[3], line[5]]

curr = start
ans = 0
i = 0
while i < len(commands):

    if commands[i] == "L":
        curr = store[curr][0]
        ans += 1
        i += 1
    else:
        curr = store[curr][1]
        ans += 1
        i += 1

    if 'ZZZ' == curr:
        print(ans)
        break

    if i == len(commands):
        i = 0


