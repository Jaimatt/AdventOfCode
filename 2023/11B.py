import time
import numpy as np
start = time.time()
i = open('11.txt').read()

space = np.asarray([[x for x in y] for y in i.split('\n')])
gapWidth = 1000000

def gaps(grid):
    new = []
    for i, x in enumerate(grid):
        if '#' not in x: new.append(i)
    return new

rowGaps = np.asarray(gaps(space))
colGaps = np.asarray(gaps(space.T))

m = np.where(space=='#')

total = 0
for x in range(len(m[0])):
    r1, c1 = m[0][x], m[1][x]
    for y in range(x):
        r2, c2 = m[0][y], m[1][y]
        rJumps = np.sum((rowGaps >= r2) & (rowGaps <= r1))
        cJumps = np.sum((colGaps >= min(c1,c2)) & (colGaps <= max(c1,c2)))
        total += abs(r1-r2) + rJumps*(gapWidth-1) + abs(c1-c2) + cJumps*(gapWidth-1)
print(total)

print("--- %s ms ---" % ((time.time() - start)*1000))