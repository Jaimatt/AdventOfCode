import time
import re
start = time.time()
i = open('1.txt').read()

c = 0
for x in i.split("\n"):
    arr = re.findall("[0-9]",x)
    c += int(arr[0])*10 + int(arr[-1])
print(c)

print("--- %s ms ---" % ((time.time() - start)*1000))