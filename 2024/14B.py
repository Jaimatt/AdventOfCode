m = open('14.txt').read()

import re

robots = [[ [int(re.findall("-{0,}[0-9]{1,}",x)[0]) for x in p.split(",")] for p in r.split(" ")] for r in m.split("\n")]

width, height = 101, 103

def update():
    for robot in robots:
        robot[0][0] = (robot[0][0] + robot[1][0])%width
        robot[0][1] = (robot[0][1] + robot[1][1])%height

def robotInSpot(x,y):
    for robot in robots:
        if robot[0] == [x,y]:
            return True
    return False

def p():
    out = ""
    for row in range(height):
        for pos in range(width):
            if robotInSpot(pos,row):
                out += "#"
            else:
                out += " "
        out += "\n"
    print(out)

print("0 seconds:")
p()
for x in range(7916):
    update()

p()
# Hah! That worked! That was pretty cool.
# How did I get the number 7916? See the helper file.

# Sidenote: My initial plan was to manually press enter until I reached the desired tree. That would have sucked going to nearly 8000!! (I gave up around 200)