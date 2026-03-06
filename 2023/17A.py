import time, heapq, math
start = time.time()
i = open('17.txt').read()

costs = [[int(y) for y in x] for x in i.split("\n")]
rows, cols = len(costs), len(costs[0])
states = {}

def cart(dir):
    dr,dc = 0,0
    if dir == 0: dr = -1
    if dir == 1: dc = 1
    if dir == 2: dr = 1
    if dir == 3: dc = -1
    return dr,dc

def visit(x):
    priority, row, col, dir, steps = x
    dr,dc = cart(dir)

    state = tuple([row,col,dir,steps])
    if state in states and states[state] <= priority: return
    states[state] = priority

    # go forward, if permitted
    if steps < 3 and row+dr in range(rows) and col+dc in range(cols):
        heapq.heappush(pq, (priority+costs[row+dr][col+dc],row+dr,col+dc,dir,steps+1))

    # turn right
    nd = (dir + 1) % 4
    dr, dc = cart(nd)
    nr, nc = row + dr, col + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        heapq.heappush(pq, (priority + costs[nr][nc], nr, nc, nd, 1))

    # turn left
    nd = (dir - 1) % 4
    dr, dc = cart(nd)
    nr, nc = row + dr, col + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        heapq.heappush(pq, (priority + costs[nr][nc], nr, nc, nd, 1))

pq = []
heapq.heappush(pq, (0,0,0,1,1))
heapq.heappush(pq, (0,0,0,2,1))

while pq:
    priority, row, col, dir, steps = heapq.heappop(pq)

    if row == rows-1 and col == cols-1:
        print(priority)
        break
    
    visit((priority, row, col, dir, steps))

print("--- %s ms ---" % ((time.time() - start)*1000))
# technically overtime at 1200ms, but good enough