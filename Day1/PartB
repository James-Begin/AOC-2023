import math

max_rgb = [0,0,0]
flag = False
ans = 0
game_num = 0
with open('inp.txt') as fp:
    contents = fp.read().splitlines()

    for line in contents:
        line = line.split()
        max_rgb = [0,0,0]
        for i in range(3, len(line), 2):
            if line[i][0] == 'g' and int(line[i-1]) > max_rgb[1]:
                max_rgb[1] = int(line[i-1])

            elif line[i][0] == 'r' and int(line[i-1]) > max_rgb[0]:
                max_rgb[0] = int(line[i-1])

            elif line[i][0] == 'b' and int(line[i-1]) > max_rgb[2]:
                max_rgb[2] = int(line[i-1])

        ans += math.prod(max_rgb)


    print(ans)
