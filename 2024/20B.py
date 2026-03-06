import time
start_time = time.time()

m = open('20.txt').read()

grid = [[c for c in r] for r in m.split('\n')]

def p():
    for row in grid:
        for c in row:
            s = str(c)
            print(" "*(3-len(s))+s,end="")
        print()
    print()

def valAt(r,c):
    if not (r in range(len(grid)) and c in range(len(grid[0]))): return '#'
    return grid[r][c]

# My idea:
# Save the index of each cell in its spot
# For every cell, chech the neighbouring cells and calc the difference
# Save the number exceeding some value

# STEP ONE: Fill the maze with values

def write(row,col,cost=0):
    grid[row][col] = cost

    for adj in [[row+1,col],[row-1,col],[row,col+1],[row,col-1]]:
        if grid[adj[0]][adj[1]] not in ['.','E']: continue
        return write(adj[0],adj[1],cost+1)
import sys
sys.setrecursionlimit(10000)
for r,row in enumerate(grid):
    for c,col in enumerate(row):
        if col == 'S':
            write(r,c)

# STEP TWO: Go through every cell and check its neighbours (within 20 jumps)
def checkNeighbours(row,col,saved=100,skips=20):
    numClose = 0

    for r in range(row-(skips+1),row+(skips+1)):
        for c in range(col-(skips+1),col+(skips+1)):
            # Skip obviously flawed cases
            if valAt(r,c) == '#': continue
            path = abs(row-r) + abs(col-c)
            if path > skips: continue
            # Save proper cases
            if abs(grid[row][col] - grid[r][c]) - path >= saved:
                numClose += 1

    return numClose

total = 0
for r,row in enumerate(grid):
    for c,col in enumerate(row):
        if col == '#': continue
        total += checkNeighbours(r,c,100,20)
        grid[r][c] = '#'

print(total)

print("--- %s seconds ---" % (time.time() - start_time))