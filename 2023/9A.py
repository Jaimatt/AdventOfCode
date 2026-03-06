import time
start = time.time()
i = open('9.txt').read()

sequences = [[int(b) for b in a.split()] for a in i.split("\n")]

def nextNum(s):
    if s.count(0) == len(s): return 0
    diffs = [s[x+1]-s[x] for x in range(len(s)-1)]
    return s[-1] + nextNum(diffs)

total = 0
for s in sequences:
    total += nextNum(s)
print(total)

print("--- %s ms ---" % ((time.time() - start)*1000))