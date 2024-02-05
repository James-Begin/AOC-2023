with open('inp.txt') as file:
    lines = file.read().splitlines()
ans = 0
directions = [[1,-1],[-1,1],[1,1],[-1,-1],[0,1],[1,0],[-1,0],[0,-1]]
visited = []
curr = []
count = 0
temp = []

for row in range(len(lines)):
    for col in range(len(lines[0])):

        if lines[row][col] == '*':

            visited = []
            for d in directions:
                curr = []
                r = row + d[0]
                c = col + d[1]
                if 0 <= r < len(lines) and 0 <= c < len(lines[0]) and [r,c] not in visited:
                    search = lines[r][c]

                    while search.isnumeric():

                        c -= 1
                        search = lines[r][c]
                        if not search.isnumeric():
                            c += 1
                            search = lines[r][c]
                            break

                    while search.isnumeric():
                        visited.append([r, c])
                        curr.append(search)
                        c += 1
                        if c == len(lines):
                            break
                        search = lines[r][c]

                    if curr:
                        temp.append(int(''.join(curr)))
                        curr = []

            if len(temp) != 2:
                temp = []
                continue
            else:
                ans += temp[0] * temp[1]
                temp = []

print(ans)
