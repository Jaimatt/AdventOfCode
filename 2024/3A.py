f = open("3.txt")
code = f.read()

# So glad I learnt about RegEx!

import re

list = re.findall("mul\\([0-9]{,3},[0-9]{,3}\\)",code)

total = 0

for x in list:
    nums = re.findall("[0-9]+",x)
    total += int(nums[0]) * int(nums[1])

print(total)