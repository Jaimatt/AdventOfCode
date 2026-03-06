f = open("1.txt")
nums = f.read().split("\n")

n = [s.split("   ") for s in nums]

nums = [[],[]]

for x in n:
    nums[0].append(int(x[0]))
    nums[1].append(int(x[1]))

nums[0].sort()
nums[1].sort()

dist = 0
for x in range(len(n)):
    dist += abs(nums[0][x]-nums[1][x])

print(dist)