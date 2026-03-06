f = open("3.txt")
code = f.read()

import re

list = re.findall("mul\\([0-9]{,3},[0-9]{,3}\\)|do\\(\\)|don't\\(\\)",code)

print(list)

total = 0
doing = True

for x in list:
    if x == "do()":
        doing = True
        continue
    if x == "don't()":
        doing = False
    if not doing:
        continue
    nums = re.findall("[0-9]+",x)
    total += int(nums[0]) * int(nums[1])

print(total)