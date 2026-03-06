import time
start = time.time()
i = open('4.txt').read()

cards = [[int(x.split(":")[0][4:])] + [[z for z in y.split(" ")] for y in x.split(":")[1].split("|")] for x in i.split("\n")]

points = 0
c = 0
while c < len(cards):
    tally = 0
    for x in cards[c][1]:
        if x == '': continue
        if x in cards[c][2]: tally += 1
    for x in range(tally):
        cards.append(cards[cards[c][0]+x])
    c+= 1
print(len(cards))

print("--- %s ms ---" % ((time.time() - start)*1000)) # long- 34s