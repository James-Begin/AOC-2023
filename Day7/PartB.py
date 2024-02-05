from collections import Counter, defaultdict

with open('inp.txt') as f:
    file = f.read().splitlines()

store = defaultdict()
ans = 0
hands = [[],[],[],[],[],[],[]]

cards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']

for line in file:

    line = line.split()
    store[line[0]] = line[1]
    count = Counter(line[0])
    c=[]
    
    if 'J' in count and count['J'] != 5:
        Js = count.pop('J')
        for k,v in count.items():
            c.append(v)
        c[c.index(max(c))] += Js
    else:
        c = count.values()
    if 5 in c:
        hands[6].append(line[0])
    elif 4 in c:
        hands[5].append(line[0])
    elif 3 in c and 2 in c:
        hands[4].append(line[0])
    elif 3 in c:
        hands[3].append(line[0])
    elif 2 in c:
        if 2 in Counter(c).values():
            hands[2].append(line[0])
        else:
            hands[1].append(line[0])
    else:
        hands[0].append(line[0])

for i in range(len(hands)):

    for _ in range(len(hands[i])):
        for k in range(len(hands[i])):
            for char in range(5):
                if k+1 < len(hands[i]):
                    if cards.index(hands[i][k][char]) > cards.index(hands[i][k+1][char]):
                        hands[i][k], hands[i][k+1] = hands[i][k+1], hands[i][k]
                        break
                    elif cards.index(hands[i][k][char]) == cards.index(hands[i][k+1][char]):
                        continue
                    else:
                        break
hands = sum(hands, [])
print(hands)
for card in range(len(hands)):
    ans += int(store[hands[card]]) * (card+1)
print(ans)

