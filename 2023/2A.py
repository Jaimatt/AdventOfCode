import time
import re
start = time.time()
i = open('2.txt').read().split('\n')

games = [[[int(re.search(r"(\d+) "+c, y).group(1)) if re.search(r"(\d+) "+c, y) else 0 for c in ['red','green','blue']] for y in x.split(": ")[1].split(";")] for x in i]

def valid(game):
    for t in game:
        if t[0] > red: return False
        if t[1] > green: return False
        if t[2] > blue: return False
    return True

red, green, blue = 12, 13, 14
possible = 0
for i, g in enumerate(games):
    if valid(g): possible += i+1
print(possible)

print("--- %s ms ---" % ((time.time() - start)*1000))