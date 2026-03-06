import time
import re
start = time.time()
i = open('3.txt').read().split("\n")

count = 0
for r, row in enumerate(i):
    nums = [(match.group(), match.start()) for match in re.finditer("\\d+", row)]

    for n in nums:
        l = len(n[0])
        ind = n[1]
        string = ""
        for k in range(r-1,r+2):
            if k < 0 or k >= len(row): continue
            string += i[k][max(ind-1,0):min(ind+l+1,len(row))]
        
        if len(re.findall("\\d|\\.",string)) != len(string):
            count += int(n[0])
print(count)

print("--- %s ms ---" % ((time.time() - start)*1000))