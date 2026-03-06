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
    corners = 0

    # loop through adjacent cells
    for adj in [[row+1,col],[row-1,col],[row,col+1],[row,col-1]]:
        # if the adjacent is in region, add its area and perimeter
        if val(adj[0],adj[1]) == s:
            call = mapOut(adj[0],adj[1])
            area += call[0]
            corners += call[1]

    # Now the yucky bit
    for adj in [[1,1],[-1,-1],[-1,1],[1,-1]]:
        if val(row+adj[0],col) in [s,s.lower()] and val(row,col+adj[1]) in [s,s.lower()] and val(row+adj[0],col+adj[1]) not in [s,s.lower()]:
            # convex corner
            corners += 1
        elif val(row+adj[0],col) not in [s,s.lower()] and val(row,col+adj[1]) not in [s,s.lower()]:
            # concave corner
            corners += 1

    return [area, corners]

counter = 0
for r, row in enumerate(garden):
    for c, col in enumerate(row):
        if col.isupper():
            region = mapOut(r,c)
            counter += region[0] * region[1]

print(counter)