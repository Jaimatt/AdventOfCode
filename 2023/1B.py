import time
import re
start = time.time()
i = open('1.txt').read()

c = 0
nums = ['','one','two','three','four','five','six','seven','eight','nine']

def toInt(x):
    if x in nums: return nums.index(x)
    return int(x)

for x in i.split("\n"):
    expression = '(?=([1-9]' + '|'.join(nums) + "))"
    arr = re.findall(expression,x)
    c += toInt(arr[0])*10 + toInt(arr[-1])
print(c)

print("--- %s ms ---" % ((time.time() - start)*1000))