import time
start = time.time()
i = open('4.txt').read()

cards = [[[z for z in y.split(" ")] for y in x.split(":")[1].split("|")] for x in i.split("\n")]

points = 0
for c in cards:
    tally = 0
    for x in c[0]:
        if x == '': continue
        if x in c[1]: tally += 1
    if tally: points += 2**(tally-1)
print(points)

print("--- %s ms ---" % ((time.time() - start)*1000))