f = open("1.txt")
nums = f.read().split("\n")

n = [s.split("   ") for s in nums]

nums = [[],[]]

for x in n:
    nums[0].append(int(x[0]))
    nums[1].append(int(x[1]))

nums[0].sort()
nums[1].sort()

score = 0

for n in nums[0]:
    score += n * nums[1].count(n)

print(score)