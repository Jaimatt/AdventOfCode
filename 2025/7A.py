def printGrid():
    for x in grid:
        for y in x:
            print(y, end="")
        print()


def project(row,column):
    global splits
    # if below is end, terminate
    # printGrid()
    if row >= len(grid)-1:
        return
    
    grid[row][column] = '|'

    # if below is blank, project there
    if grid[row+1][column] == '.':
        project(row+1,column)

    # if below is splitter, split
    elif grid[row+1][column] == '^':
        project(row+1,column-1)
        project(row+1,column+1)
        splits += 1

    # if below is already a beam, terminate
    elif grid[row+1][column] == '|':
        return


f = open("7_input.txt")
grid = f.read().split("\n")

for x in range(len(grid)):
    grid[x] = list(grid[x])

# find S
sCol = grid[0].index("S")

global splits
splits = 0

printGrid()
project(0,sCol)
printGrid()
print(splits)