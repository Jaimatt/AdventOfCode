f = open("4_input.txt")
grid = f.read().split("\n")

for x in range(len(grid)):
    grid[x] = list(grid[x])

print(grid)

def spotChecker(row,cell):
    # out of range: return false
    if row<0:
        return 0
    if row>=len(grid):
        return 0
    if cell<0:
        return 0
    if cell>=len(grid[0]):
        return 0
    
    # now check if a cell is a package
    if grid[row][cell] == '@':
        return 1
    else:
        return 0
    
global removed
removed = 0

def removePossibles():
    global removed
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            # print(grid[row][cell])
            
            # skip blanks
            if grid[row][cell] == '.':
                continue

            # check neighbours
            adjacent = 0
            adjacent += spotChecker(row-1,cell)
            adjacent += spotChecker(row-1,cell-1)
            adjacent += spotChecker(row-1,cell+1)
            adjacent += spotChecker(row,cell-1)
            adjacent += spotChecker(row,cell+1)
            adjacent += spotChecker(row+1,cell-1)
            adjacent += spotChecker(row+1,cell)
            adjacent += spotChecker(row+1,cell+1)

            # print(adjacent)

            if (adjacent<4):
                grid[row][cell] = '.'
                removed += 1

oldRemoved = -1

while removed > oldRemoved:
    oldRemoved = removed
    removePossibles()

print("total:")
print(removed)