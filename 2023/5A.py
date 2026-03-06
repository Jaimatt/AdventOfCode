import time
start = time.time()
i = open('5.txt').read().split('\n\n')

seeds = [int(x) for x in i[0].split(": ")[1].split(" ")]
maps = [[[int(z) for z in y.split(' ')] for y in x.split('\n')[1:]] for x in i[1:]]

def parseMap(val, mapId):
    map = maps[mapId]
    for m in map:
        if val >= m[1] and val - m[1] < m[2]: return val - m[1] + m[0]
    return val

for k in range(len(maps)):
    for i, s in enumerate(seeds):
        seeds[i] = parseMap(s,k)
print(min(seeds))

print("--- %s ms ---" % ((time.time() - start)*1000))