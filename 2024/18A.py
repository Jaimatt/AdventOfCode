import time
start_time = time.time()

m = open('18.txt').read()
import math

dim = 71
kilobyte = 1024

grid = [['.' for x in range(dim)] for y in range(dim)]

for a in m.split('\n')[:kilobyte]:
    pos = [int(i) for i in a.split(',')]
    grid[pos[1]][pos[0]] = '#'

def p():
    for row in grid:
        for c in row:
            s = str(c)
            print(" "*(3-len(s))+s,end=" ")
        print()
    print()

def node(row,col):
    if not (row in range(dim) and col in range(dim)): return '#'
    v = grid[row][col]
    return math.inf if v == '.' else v

def dijkstra(row,col,cost):
    # base: cease path if cannot beat cost
    if node(row,col) <= cost:
        return

    # work: save the new cost
    if node(row,col) > cost:
        grid[row][col] = cost

    # recursive call: visit neighbour nodes
    for adj in [[row+1,col],[row-1,col],[row,col-1],[row,col+1]]:
        if node(adj[0], adj[1]) == '#': continue
        dijkstra(adj[0], adj[1], cost + 1)

# Grid is too big: had to increase the recursion limit!
import sys
sys.setrecursionlimit(3000)

# Run the algorithm from start, read end cost
dijkstra(0,0,0)
print(grid[dim-1][dim-1])

print("--- %s seconds ---" % (time.time() - start_time))