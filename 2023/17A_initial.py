import time, heapq, math
start = time.time()
i = open('17_test.txt').read()

costs = [[int(y) for y in x] for x in i.split("\n")]
paths = [[[math.inf for y in x] for x in i.split("\n")] for m in range(4)]

def val(row,col):
    if not (row in range(len(costs)) and col in range(len(costs[0]))): return math.inf
    else: return costs[row][col]

def cart(dir):
    dr,dc = 0,0
    if dir == 0: dr = -1
    if dir == 1: dc = 1
    if dir == 2: dr = 1
    if dir == 3: dc = -1
    return dr,dc


def visit(x):
    priority, row, col, dir, straights = x

    dr,dc = cart(dir)


    # don't bother if you've already found cheaper
    if priority==math.inf or paths[dir][row][col] <= priority: return
    paths[dir][row][col] = priority

    # go forward, if permitted
    if straights < 3:
        heapq.heappush(pq, (priority+val(row+dr,col+dc),row+dr,col+dc,dir,straights+1))
    # go RL
    heapq.heappush(pq, (priority+val(row+dc,col-dr),row+dc,col-dr,(dir+1)%4,1))
    heapq.heappush(pq, (priority+val(row-dc,col+dr),row-dc,col+dr,(dir-1)%4,1))

pq = []

visit((0,0,0,1,0))

while len(pq):
    visit(heapq.heappop(pq))
    if [paths[x][len(costs)-1][len(costs[0])-1] for x in range(4)] != [math.inf for x in range(4)]:
        break
print(min([paths[x][len(costs)-1][len(costs[0])-1] for x in range(4)]))

print("--- %s ms ---" % ((time.time() - start)*1000))