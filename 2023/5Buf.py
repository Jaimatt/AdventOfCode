import time
start = time.time()
i = open('5_test.txt').read().split('\n\n')

seeds = [int(x) for x in i[0].split(": ")[1].split(" ")]
seeds = [[seeds[2*k],seeds[2*k+1]] for k in range(int(len(seeds)/2))]
maps = [[[int(z) for z in y.split(' ')] for y in x.split('\n')[1:]] for x in i[1:]]

def sb(n): return lambda x : x[n]
for m in maps: m.sort(key=sb(1))

print(seeds)
print(maps)

def parseMap(vals, mapId):
    # vals = [min, size], max = min+size
    map = maps[mapId]
    for m in map:
        # if contained within range entirely
        diff = m[0] - m[1]
        if vals[0] >= m[1] and vals[1] <= vals[0]-m[2]:
            return [[vals[0]+diff,vals[1]]]
        
        # if spills over right
        elif vals[0] >= m[1] and vals[1] > m[2]:
            return [[vals[0]+diff,m[2]-vals[0]]] + parseMap([m[1]+m[2],vals[1]-m[2]],mapId)
        
    return [vals]

# for k in range(len(maps)):
seeds = [[90,9]]
newSeeds = []
for i, s in enumerate(seeds):
    newSeeds += parseMap(s,0)
# seeds = newSeeds
print(newSeeds)

print("--- %s ms ---" % ((time.time() - start)*1000))




# most of the above is garbage :/