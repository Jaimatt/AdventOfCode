import time
start = time.time()
i = open('4.txt').read()

cards = [[int(x.split(":")[0][4:])] + [[z for z in y.split(" ")] for y in x.split(":")[1].split("|")] for x in i.split("\n")]

cardScore = []

for c in cards:
    score = 0
    for x in c[1]:
        if x == '': continue
        if x in c[2]: score += 1
    cardScore.append([score,1])

def calcCards(n):
    score, qty = cardScore[n][0], cardScore[n][1]
    for x in range(score):
        cardScore[n+1+x][1] += qty
    return qty

total = 0
for x in range(len(cards)):
    total += calcCards(x)
print(total)

print("--- %s ms ---" % ((time.time() - start)*1000))
# down from 30s to 3ms !!
# i.e. I optimised it by like 10000x