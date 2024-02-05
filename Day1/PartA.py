max_rgb = [12,13,14]
flag = False
ans = 0
game_num = 0
with open('inp.txt') as fp:
    contents = fp.read().splitlines()

    for line in contents:
        flag = False
        line = line.split()

        game_num += 1

        for i in range(3, len(line), 2):
        
            if line[i][0] == 'g' and int(line[i-1]) > max_rgb[1]:
                flag = True
                break
            elif line[i][0] == 'r' and int(line[i-1]) > max_rgb[0]:
                flag = True
                break
            elif line[i][0] == 'b' and int(line[i-1]) > max_rgb[2]:
                flag = True
                break

        if not flag:
            ans += game_num

    print(ans)

