import math

f = open("8_input.txt")
junctions = f.read().split("\n")

n = len(junctions)

for j in range(n):
    junctions[j] = junctions[j].split(",")
    for k in range(3):
        junctions[j][k] = int(junctions[j][k])

def distance(d):
    p1 = junctions[d[0]]
    p2 = junctions[d[1]]
    
    squared_diffs = [(c2 - c1)**2 for c1, c2 in zip(p1, p2)]
    return math.sqrt(sum(squared_diffs))

paths = []
for a in range(n):
    for b in range(a):
        paths.append([a,b])

paths.sort(key=distance)

pathNum = 1000

# store all networks
networks = []
for p in range(pathNum):
    path = set(paths[p])
    unionIndexes = []
    for k in range(len(networks)):
        if not networks[k].isdisjoint(path):
            unionIndexes.append(k)

    if len(unionIndexes) == 0:
        networks.append(path)
    elif len(unionIndexes) == 1:
        networks[unionIndexes[0]] = networks[unionIndexes[0]] | path
    elif len(unionIndexes) == 2:
        networks[unionIndexes[0]] = networks[unionIndexes[0]] | networks[unionIndexes[1]] | path
        networks.pop(unionIndexes[1])

print(networks)

# Now we have a list of disjoint sets. We must calculate the product of the sizes of the three largest
sizes = []
for s in networks:
    sizes.append(len(s))

sizes.sort(reverse=True)

print(sizes)

print(sizes[0]*sizes[1]*sizes[2])