import time
start_time = time.time()

m = open('20.txt').read()

grid = [[c if c == '#' else '.' for c in r] for r in m.split('\n')]

def p():
    for row in grid:
        for c in row:
            print(c,end="")
        print()
    print()

# searcher function:
def wall(row,col):
    if not (row in range(len(grid)) and col in range(len(grid[0]))):
        return True
    return grid[row][col] in ['O','#']

# distance function:
def dist(a,b):
    distance = distHelper(a,b,0)

    for r,row in enumerate(grid):
        for c,col in enumerate(row):
            if col=='O': grid[r][c] = '.'

    return distance

def distHelper(a,b,d):
    # base case: end
    if a == b:
        return d
    
    # work
    grid[a[0]][a[1]] = 'O'

    # recursive case: move
    rv = 0
    for adj in [[a[0]+1,a[1]],[a[0]-1,a[1]],[a[0],a[1]-1],[a[0],a[1]+1]]:
        if wall(adj[0], adj[1]): continue
        rv += distHelper(adj,b,d+1)
    
    return rv

# Grid is too big: had to increase the recursion limit!
import sys
sys.setrecursionlimit(10000)

count = 0
goal = 100
# Loop through every grid item
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        # don't bother if it isn't a wall
        if not wall(r,c): continue

        # Side Skip Check
        if (not wall(r+1,c)) and (not wall(r-1,c)):
            count += dist([r+1,c],[r-1,c])-2 >= goal

        # Top Skip Check
        if (not wall(r,c+1)) and (not wall(r,c-1)):
            count += dist([r,c+1],[r,c-1])-2 >= goal

print(count)
print("--- %s seconds ---" % (time.time() - start_time))