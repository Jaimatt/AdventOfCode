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

def allConnected():
    if not len(networks) == 1:
        return False
    if not len(networks[0]) == n:
        return False
    return True

paths = []
for a in range(n):
    for b in range(a):
        paths.append([a,b])

paths.sort(key=distance)

# store all networks
networks = []
p=0
while not allConnected():
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
    p+=1

print(networks)
print(paths[p-1])
print(junctions[paths[p-1][0]][0]*junctions[paths[p-1][1]][0])