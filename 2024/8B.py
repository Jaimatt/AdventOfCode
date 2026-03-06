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
        
        # we have selected an antenna
        for r2, row2 in enumerate(antennas):
            for c2, col2 in enumerate(row2):
                if r == r2 and c == c2:
                    continue
                if col == col2:
                    for k in range(100):
                        antinode((k+1)*r-k*r2,(k+1)*c-k*c2)
                        antinode((k+1)*r2-k*r,(k+1)*c2-k*c)

count = 0
for r in antinodes:
    for c in r:
        count += c=="#"
p(antinodes)
print(count)