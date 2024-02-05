with open('inp.txt') as file:
    lines = file.read().splitlines()
count = 0
win = []
have = []
ans = 0
curr = 0

card_num = 1

cards = [1] * len(lines)
print(cards)
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

    print(count)
    for w in range(count):
        if card_num + w >= len(cards):
            break

        cards[card_num + w] += cards[card_num-1]
    print(cards)
    curr = 0
    card_num += 1


    count = 0

print(sum(cards))



