import time, math, sys
from functools import reduce
start = time.time()
sys.setrecursionlimit(30000)
i = open('8.txt').read().split('\n\n')

directions = i[0]
graph = {x.split(" = ")[0] : {['L','R'][i]:y for i,y in enumerate(x.split(" = ")[1][1:-1].split(", "))} for x in i[1].split('\n')}

def traverse(node,steps=0):
    if node[2] == 'Z': return steps
    d = directions[steps%len(directions)]
    return traverse(graph[node][d],steps+1)

# By testing, it seems all points visit their respective end point periodically.
# We can leverage this by finding the no. of their first visit, and then the lcm of these values
starters = []
for x in graph:
    if x[2] == 'A': starters.append(x)

ans = reduce(math.lcm, [traverse(x) for x in starters])
print(ans)

print("--- %s ms ---" % ((time.time() - start)*1000))