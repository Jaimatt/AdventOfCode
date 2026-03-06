import time
start = time.time()
i = open('18.txt').read()

steps = [[j.split(" ")[0], int(j.split(" ")[1])] for j in i.split('\n')]

area = 0
perimeter = 0
x,y = 0,0

# Using Shoelace Formula https://en.wikipedia.org/wiki/Shoelace_formula#Other_formulas_2
for s in steps:
    x2,y2 = x,y
    if s[0] == 'U': y2 += s[1]
    if s[0] == 'D': y2 -= s[1]
    if s[0] == 'R': x2 += s[1]
    if s[0] == 'L': x2 -= s[1]
    perimeter += s[1]
    area += (x*y2-x2*y)/2
    x,y = x2,y2

# This uses Pick's theorem https://en.wikipedia.org/wiki/Pick%27s_theorem
print(int(abs(area) + perimeter/2 + 1))

print("--- %s ms ---" % ((time.time() - start)*1000))