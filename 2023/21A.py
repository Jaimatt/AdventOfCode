import time
start = time.time()
i = open('21.txt').read()

garden = [[y for y in x] for x in i.split('\n')]

def p(g):
    for row in g:
        for c in row:
            print(c,end=" ")
        print()
    print()

def val(r,c):
    if not (r in range(len(garden)) and c in range(len(garden[0]))): return '#'
    return newGarden[r][c]

def walk(row,col):
    count = 0
    for adj in [[1,0],[0,1],[-1,0],[0,-1]]:
        if val(row+adj[0],col+adj[1]) == '.': 
            count += 1
            newGarden[row+adj[0]][col+adj[1]] = 'S'
    return count

for k in range(64):
    count = 0
    newGarden = [[y if y=='#' else '.' for y in x] for x in i.split('\n')]
    for r,row in enumerate(garden):
        for c,col in enumerate(row):
            if col == "S": count += walk(r,c)
    garden = newGarden
print(count)

print("--- %s ms ---" % ((time.time() - start)*1000))