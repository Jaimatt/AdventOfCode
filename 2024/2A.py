import math

f = open("2.txt")
reportList = f.read().split("\n")

def checkSafety(report):
    gaps = []
    for x in range(len(report)-1):
        gaps.append(int(report[x+1])-int(report[x]))
    
    if max(gaps) >= 4 or min(gaps) <= -4:
        return 0

    if max(gaps) >= 0 and min(gaps) <= 0:
        return 0
    
    return 1

count = 0
for x in reportList:    
    count += checkSafety(x.split(" "))
print(count)