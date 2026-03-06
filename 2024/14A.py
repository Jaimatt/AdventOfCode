m = open('14.txt').read()

import re

robots = [[ [int(re.findall("-{0,}[0-9]{1,}",x)[0]) for x in p.split(",")] for p in r.split(" ")] for r in m.split("\n")]

width, height = 101, 103

def update():
    for robot in robots:
        robot[0][0] = (robot[0][0] + robot[1][0])%width
        robot[0][1] = (robot[0][1] + robot[1][1])%height

def countInRange(xmin,xmax,ymin,ymax):
    count = 0
    for robot in robots:
        if not robot[0][0] in range(xmin,xmax):
            continue
        if not robot[0][1] in range(ymin,ymax):
            continue
        count += 1
    return count

for x in range(100):
    update()

val = 1
val *= countInRange(0,int(width/2),0,int(height/2))
val *= countInRange(int(width/2)+1,width,0,int(height/2))
val *= countInRange(0,int(width/2),int(height/2)+1,height)
val *= countInRange(int(width/2)+1,width,int(height/2)+1,height)
print(val)