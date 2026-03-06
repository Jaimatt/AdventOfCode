import time
import math
import sys
start_time = time.time()

# Maze is too big: had to increase the recursion limit!
sys.setrecursionlimit(10000)

m = open('16.txt').read().split("\n\n")
maze = [[[x if x == '#' else '.' for x in row] for row in m[0].split("\n")] for k in range(5)]
# There are 5 copies of the maze, each for a direction you could travel in (except #5)
# 0 = up, 1 = right, 2 = down, 3 = left, 4=notetaking purposes only

# Printing function; straightforward
def p():
    for d, direction in enumerate(maze):
        print(d)
        for row in direction:
            for c in row:
                s = str(c)
                print(" "*(5-len(s))+s,end=" ")
            print()
        print()

# Get value at some given node. (walls on border so don't need to worry about out-of-bounds requests)
def node(row,col,dir):
    v = maze[dir][row][col]
    return math.inf if v == '.' else v

# From vector direction, get maze matrix index
def dir(dr,dc):
    if dr==-1 and dc==0: return 0
    if dr==0 and dc==1: return 1
    if dr==1 and dc==0: return 2
    if dr==0 and dc==-1: return 3

# Dijkstra's Algorithm!
def dijkstra(row,col,drow,dcol,cost):
    # Base Case: cease path if cannot beat cost or is a wall
    me = node(row,col,dir(drow,dcol))
    if me == '#' or me <= cost:
        return

    # Work: save the new cost to the matrix (in the correct copy, as per direction)
    if me > cost:
        maze[dir(drow,dcol)][row][col] = cost

    # Move within maze; go forward:
    dijkstra(row+drow,col+dcol,drow,dcol,cost+1)

    # Turn left on the spot; i.e. move to a parallel maze:
    dijkstra(row,col,-dcol,drow,cost+1000)

    # right
    dijkstra(row,col,+dcol,-drow,cost+1000)

# Run the algorithm from start, read end cost
dijkstra(len(maze[0])-2,1,0,1,0)
ends = [] # ends will differ based on direction
for x in maze[:4]: ends.append(x[1][len(x[0])-2])
print(min(ends)) # the cheapest way of getting to the end

# New Search Function: Backtrack.
# Backtrack will go through paths that got to end in cheapest way possible
def backtrack(row,col,drow,dcol,cost):
    me = node(row,col,dir(drow,dcol))

    # Base Case: do nothing if wall, or costs more than expected cost (cost)
    # If costs more than expected cost, this node is not on an ideal path
    if me == '#' or me > cost: return

    # Work: write an 'O' to signify this is on an optimal path
    maze[4][row][col] = 'O'

    # Travel backwards, -1 cost
    backtrack(row-drow,col-dcol,drow,dcol,cost-1)

    # turn right/ turn left -1000 cost
    backtrack(row,col,-dcol,drow,cost-1000)
    backtrack(row,col,dcol,-drow,cost-1000)

# Get info relating to the end state
e = min(ends)
d = ends.index(e)
dr, dc = int(-math.cos((d*math.pi)/2)), int(math.sin((d*math.pi)/2))

# Run backtrack
backtrack(1,len(maze[0][0])-2,dr,dc,e)

# Count the O's, i.e. spots on optimal routes
count = 0
for r in range(len(maze[0])):
    for c in range(len(maze[0][0])):
        if maze[4][r][c] == 'O': count += 1
print(count)

# Show how BAD my algorithm is (~100s, I didn't use PQs)
print("--- %s seconds ---" % (time.time() - start_time))