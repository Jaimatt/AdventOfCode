import time
import re
start = time.time()
i = open('2.txt').read().split('\n')

games = [[[int(re.search(r"(\d+) "+c, y).group(1)) if re.search(r"(\d+) "+c, y) else 0 for c in ['red','green','blue']] for y in x.split(": ")[1].split(";")] for x in i]

def power(game):
    r,g,b = 0,0,0
    for t in game:
        r = max(r,t[0])
        g = max(g,t[1])
        b = max(b,t[2])
    return r*g*b

possible = 0
for i, g in enumerate(games):
    possible += power(g)
print(possible)

print("--- %s ms ---" % ((time.time() - start)*1000))