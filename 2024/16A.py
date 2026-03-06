m = open('16.txt').read().split("\n\n")

import math

maze = [[x if x == '#' else '.' for x in row] for row in m[0].split("\n")]

def p():
    for row in maze:
        for c in row:
            s = str(c)
            print(" "*(5-len(s))+s,end=" ")
        print()
    print()

def node(row,col):
    v = maze[row][col]
    return math.inf if v == '.' else v

def dijkstra(row,col,dir,cost):
    # base: cease path if cannot beat cost
    if node(row,col) <= cost:
        return

    # work: save the new cost
    if node(row,col) > cost:
        maze[row][col] = cost

    # recursive call: visit neighbour nodes
    for adj in [["v",row+1,col],["^",row-1,col],["<",row,col-1],[">",row,col+1]]:
        turning = 1000
        if not node(adj[1], adj[2]) == '#':
            if dir == adj[0]: turning = 0
            dijkstra(adj[1], adj[2], adj[0], cost + 1 + turning)

# Maze is too big: had to increase the recursion limit!
import sys
sys.setrecursionlimit(3000)

# Run the algorithm from start, read end cost
dijkstra(len(maze)-2,1,'>',0)
print(maze[1][len(maze[0])-2])