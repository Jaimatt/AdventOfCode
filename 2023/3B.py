import time
import re
start = time.time()
i = open('3.txt').read().split("\n")

ratios = 0
for r,row in enumerate(i):
    for c,col in enumerate(row):
        if col != '*': continue
        # we are at a *, time to check if it's a gear
        adjNums = []
        for adjacentrow in [r-1,r,r+1]:
            if adjacentrow not in range(len(i)): continue
            nums = [(match.group(), match.start(), match.end()) for match in re.finditer("\\d+", i[adjacentrow])]
            # now check if each num is appropriately positioned
            for n in nums:
                if set(range(c-1,c+2)) & set(range(n[1],n[2])):
                    adjNums.append(int(n[0]))
        if len(adjNums) == 2: ratios += adjNums[0]*adjNums[1]
print(ratios)

print("--- %s ms ---" % ((time.time() - start)*1000))