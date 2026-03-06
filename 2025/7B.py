import time


def printGrid():
    stringForm = ""
    for x in grid:
        for y in x:
            # if y == '.' or y == '^':
            #     stringForm += y
            # else:
            #     stringForm += '|'
            # stringForm += ' '
            stringForm += str(y) + ' '
        stringForm += "\n"
    print("\x1b[2J\x1b[H", end="")
    print(stringForm)


def project(row,column):
    # if already calculated, return the existing value
    if grid[row][column] != '.':
        return grid[row][column]

    # if below is end, terminate
    if row >= len(grid)-1:
        grid[row][column] = 1
    # if below is splitter, split
    elif grid[row+1][column] == '^':
        grid[row][column] = project(row+1,column+1) + project(row+1,column-1)
    # otherwise just continue to next
    else:
        grid[row][column] = project(row+1,column)

    # and return the value
    printGrid()
    # time.sleep(0.1)
    return grid[row][column]


f = open("7_input.txt")
grid = f.read().split("\n")

for x in range(len(grid)):
    grid[x] = list(grid[x])

# find S, then delete it
sCol = grid[0].index("S")
grid[0][sCol] = '.'

input("Enter to Start...")

printGrid()
timelines = project(0,sCol)
print(timelines)
# printGrid()
input()