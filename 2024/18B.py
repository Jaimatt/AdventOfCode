import time
start_time = time.time()

m = open('18.txt').read()

dim = 71
kilobyte = 1024

grid = [['.' for x in range(dim)] for y in range(dim)]
falling = m.split('\n')

for a in falling[:kilobyte]:
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
    if not (row in range(dim) and col in range(dim)): return False
    return grid[row][col] == '.'

def dfs(row,col):
    # work: mark visited
    grid[row][col] = 'O'

    # recursive call: visit neighbour nodes
    for adj in [[row+1,col],[row-1,col],[row,col-1],[row,col+1]]:
        if not node(adj[0], adj[1]): continue
        dfs(adj[0], adj[1])

# Grid is too big: had to increase the recursion limit!
import sys
sys.setrecursionlimit(3000)

# Run the algorithm from start, read end cost
for addPos in falling[kilobyte-1:]:
    # Add the new wall
    pos = [int(i) for i in addPos.split(',')]
    grid[pos[1]][pos[0]] = '#'

    # Remove nums from grid
    for r in range(dim):
        for c in range(dim):
            if grid[r][c] == 'O': grid[r][c] = '.'

    # Run Depth First Search
    dfs(0,0)
    end = grid[dim-1][dim-1]
    if end == '.':
        print(addPos)
        break

print("--- %s seconds ---" % (time.time() - start_time))