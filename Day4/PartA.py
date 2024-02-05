with open('inp.txt') as file:
    lines = file.read().splitlines()
count = 0
win = []
have = []
ans = 0
for line in lines:
    line = line.split()

    i = 2
    while line[i] != "|":
        if line[i].isnumeric():
            win.append(int(line[i]))
        i += 1
    for k in range(i, len(line)):
        if line[k].isnumeric():
            have.append(int(line[k]))

    for j in win:
        if j in have:
            count += 1

    win = []
    have = []
    if count != 0:
        ans += 2 ** (count-1)

    count = 0
print(ans)



