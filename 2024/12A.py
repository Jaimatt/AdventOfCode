m = open('12.txt').read()

garden = [[x for x in y] for y in m.split("\n")]

def p():
    for row in garden:
        for c in row:
            print(c,end="")
        print()
    print()

def val(row,col):
    if not (col in range(len(garden[0])) and row in range(len(garden))):
        return "#"
    return garden[row][col]

def mapOut(row,col):
    # get cell value and mark as searched
    s = garden[row][col]
    garden[row][col] = s.lower()

    area = 1
    perimeter = 0

    # loop through adjacent cells
    for adj in [[row+1,col],[row-1,col],[row,col+1],[row,col-1]]:
        # if the adjacent is in region, add its area and perimeter
        if val(adj[0],adj[1]) == s:
            call = mapOut(adj[0],adj[1])
            area += call[0]
            perimeter += call[1]

        # if the adjacent is not in region, add one to perimeter
        elif not val(adj[0],adj[1]) == s.lower():
            perimeter += 1

    return [area, perimeter]

counter = 0
for r, row in enumerate(garden):
    for c, col in enumerate(row):
        if col.isupper():
            region = mapOut(r,c)
            counter += region[0] * region[1]

print(counter)