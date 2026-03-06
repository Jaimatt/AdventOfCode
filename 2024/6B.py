import time
start_time = time.time()

a = open('6.txt').read()
grid = [[i for i in j] for j in a.split('\n')]
 
height = len(grid)
width = len(grid[0])

for r,row in enumerate(grid):
    for c,col in enumerate(row):
        if col == '^':
            sy,sx = r,c
            grid[r][c] = '.'

y = sy
x = sx
dy = -1
dx = 0

def wallAt(c,r):
    if not (c in range(width) and r in range(height)):
        return False
    return grid[r][c] == "#" or grid[r][c] == '@'
    
def p():
    for r in grid:
        for c in r:
            print(c,end="")
        print()
    print()

def inRegion():
    return x in range(width) and y in range(height)

def dirSymbol():
    if dx == 0 and dy == 1:
        return 'v'
    if dx == 0 and dy == -1:
        return '^'
    if dx == -1 and dy == 0:
        return '<'
    if dx == 1 and dy == 0:
        return '>'

def traverse():
    global x, y, dx, dy
    iterations = 0
    while inRegion():
        # If we've just arrived at a loop, flag it.
        if grid[y][x] == dirSymbol():
            return True
        
        # While we're unable to move...
        while wallAt(x+dx,y+dy):
            # rotate 90 degrees
            dx,dy = -dy,dx
            pass

        # Place your marker
        grid[y][x] = dirSymbol()

        # ..And move forward!
        x = x + dx
        y = y + dy

        iterations += 1
        # Emergency breaks:
        if iterations > width*height:
            print("emergency breaks used")
            return True

    # We've escaped, so say 'false' i.e. not stuck in a loop
    return False

counter = 0
# run through every possible position and note weather it would cause a loop
for r,row in enumerate(grid):
    for c,col in enumerate(row):
        # skip those that are already walls
        if grid[r][c] == '#': continue

        # reset the arena
        x,y,dx,dy = sx,sy,0,-1
        grid = [[i for i in j] for j in a.split('\n')]
        grid[sy][sx] = '.'
        grid[r][c] = '@'

        
        m = traverse()
        # print(r,c,m)
        counter += m

print(counter)
print("--- %s seconds ---" % (time.time() - start_time))