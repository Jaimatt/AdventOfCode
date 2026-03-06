import time,re
start = time.time()
i = open('12.txt').read()

springs = [[x.split(" ")[0], [int(y) for y in x.split()[1].split(",")]] for x in i.split("\n")]

def analyse(spring,groups):
    if '?' not in spring:
        g = [len(x) for x in re.findall("#+",spring)]
        return g == groups

    count = 0
    count += analyse(spring.replace('?','#',1),groups,)
    count += analyse(spring.replace('?','.',1),groups)
    return count

total = 0
for s in springs:
    total += analyse(s[0],s[1])
print(total)

print("--- %s ms ---" % ((time.time() - start)*1000))
# Runs in around 11 seconds (over time)