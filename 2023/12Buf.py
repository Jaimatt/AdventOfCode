import time,re
start = time.time()
i = open('12_test.txt').read()

springs = [['?'.join([x.split(" ")[0]]*5), [int(y) for y in x.split()[1].split(",")]*5] for x in i.split("\n")]

print(springs[0])

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
    print(s)
    total += analyse(s[0],s[1])
    pass
print(total)

print("--- %s ms ---" % ((time.time() - start)*1000))