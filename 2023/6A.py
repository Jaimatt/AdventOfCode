import time
import re
start = time.time()
i = open('6.txt').read()

times = [int(x) for x in re.findall("\\d+",i.split('\n')[0])]
dists = [int(x) for x in re.findall("\\d+",i.split('\n')[1])]

val = 1
for k in range(len(times)):
    recordBeaters = 0
    # try all hold times
    for h in range(times[k]):
        d = (times[k] - h)*h
        if d > dists[k]: recordBeaters += 1
    val *= recordBeaters
print(val)

print("--- %s ms ---" % ((time.time() - start)*1000))