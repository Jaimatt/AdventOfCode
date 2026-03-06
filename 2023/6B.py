import time, re, math
start = time.time()
i = open('6.txt').read()

t = int(''.join(re.findall("\\d+",i.split('\n')[0])))
r = int(''.join(re.findall("\\d+",i.split('\n')[1])))

root1, root2 = t/2 - math.sqrt(t**2 - 4*r)/2, t/2 + math.sqrt(t**2 - 4*r)/2
print(math.floor(root2) - math.ceil(root1) + 1)

print("--- %s ms ---" % ((time.time() - start)*1000))