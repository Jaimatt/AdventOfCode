import time
start_time = time.time()

m = open('16.txt').read().split("\n\n")

import math

maze = [[x if x in ['#','E'] else '.' for x in row] for row in m[0].split("\n")]
w = len(maze[0])

endCost = 66404
# endCost = 11048

def p():
    for row in maze:
        for c in row:
            print(c,end=" ")
        print()
    print()

def node(row,col):
    v = maze[row][col]
    return math.inf if v[0] == '.' else v[0]

def dijkstra(row,col,drow,dcol,cost):
    # base: if at end of maze, return whether we did it at cost
    # (i.e return true if this is a valid path)
    if node(row,col) == 'E':
        return cost == endCost

    # base: reasons to cancel: accrued too much cost.
    if cost > endCost or node(row,col) == 'x' or node(row,col) == '#':
        return False
    
    maze[row][col] = 'x'

    # forwards
    c1 = dijkstra(row+drow, col+dcol, drow, dcol, cost + 1)

    # lr
    c2 = dijkstra(row-dcol,col+drow,-dcol,drow,cost+1+1000)
    c3 = dijkstra(row+dcol,col-drow,+dcol,-drow,cost+1+1000)
    
    if c1 or c2 or c3:
        maze[row][col] = 'O'
    else:
        maze[row][col] = '.'

    return c1 or c2 or c3

# Maze is too big: had to increase the recursion limit!
import sys
sys.setrecursionlimit(3000)

# Run the algorithm from start, read end cost
dijkstra(len(maze)-2,1,0,1,0)
p()

# Now, count the number of points
count = 1
for r in maze: 
    for c in r: count += c=='O'
print(count)

print("--- %s seconds ---" % (time.time() - start_time))