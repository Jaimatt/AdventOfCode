i = open('8.txt').read()

antennas = [[x for x in row] for row in i.split("\n")]
antinodes = [['.' for x in row] for row in i.split("\n")]

def p(grid):
    for row in grid:
        for c in row:
            print(c,end="")
        print()
    print()

def antinode(r,c):
    if not (r in range(len(antinodes)) and c in range(len(antinodes[0]))): return
    antinodes[r][c] = '#'

for r, row in enumerate(antennas):
    for c, col in enumerate(row):
        if col == '.':
            continue
        
        antennas[r][c] = '.'
        # we have selected an antenna
        for r2, row2 in enumerate(antennas):
            for c2, col2 in enumerate(row2):
                if col == col2:
                    antinode(2*r-r2,2*c-c2)
                    antinode(2*r2-r,2*c2-c)

count = 0
for r in antinodes:
    for c in r:
        count += c=="#"
print(count)