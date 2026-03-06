m = open('15.txt').read().split("\n\n")

warehouse = []

for r in m[0].split('\n'):
    row = []
    for x in r:
        if x in ['#','.']: row += [x,x]
        if x == 'O': row += ['[',']']
        if x == '@': row += ['@','.']
    warehouse.append(row)


instructions = [i for i in ''.join(m[1].split("\n"))]

def p():
    for row in warehouse:
        for c in row:
            print(c,end="")
        print()
    print()

def robotPos():
    for r, row in enumerate(warehouse):
        for c, col in enumerate(row):
            if col == "@": return r,c

def score():
    count = 0
    for r, row in enumerate(warehouse):
        for c, col in enumerate(row):
            if col == "[":
                count += 100 * r + c
    return count

def immovableScanner(row,col,y):
    # base:
    if y == 0:
        return False
    if warehouse[row + y][col] == "#":
        return True
    
    if warehouse[row + y][col] == ".":
        return False

    # recurse:    
    side = 92 - ord(warehouse[row+y][col])
    return immovableScanner(row+y,col+side,y) or immovableScanner(row+y,col,y)

def moveItem(row, col, dir):
    # Specify the direction we're going
    x,y = 0,0
    if dir == "v": y=1
    if dir == "^": y=-1
    if dir == "<": x=-1
    if dir == ">": x=1

    # if we're going to a wall, cease work
    if warehouse[row + y][col + x] == '#':
        return
    
    # if we're a box moving vertically, and either side are going into a wall, cease work
    if immovableScanner(row,col,y):
        return
    
    # if it's a box, attempt to push it
    if warehouse[row + y][col + x] in ['[',']']:
        # if we're a wall moving vertically, push the other side of the box
        if not y == 0:
            side = 92 - ord(warehouse[row + y][col + x])
            moveItem(row + y, col + x + side, dir)

        moveItem(row + y, col + x, dir)

    # if there's empty space, push yourself into it
    if warehouse[row + y][col + x] == '.':
        warehouse[row + y][col + x], warehouse[row][col] = warehouse[row][col], warehouse[row + y][col + x]

p()
for i in instructions:
    r,c = robotPos()
    moveItem(r,c,i)

print(score())