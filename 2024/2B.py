import math

f = open("2.txt")
reportList = f.read().split("\n")

def checkSafety(report,damp):
    print("testing: ")
    print(report)

    print("testing buffers...")
    # safety dampener:
    for x in range(len(report)):
        if damp and checkSafety(report[:x]+report[x+1:],False):
            return 1

    gaps = []
    for x in range(len(report)-1):
        gaps.append(int(report[x+1])-int(report[x]))
    
    if max(gaps) >= 4 or min(gaps) <= -4:
        print("aborted")
        return 0

    if max(gaps) >= 0 and min(gaps) <= 0:
        print("aborted")
        return 0
    
    print("success")
    return 1

count = 0
for x in reportList:    
    count += checkSafety(x.split(" "),True)
print(count)

# THE ABOVE IS THE MOST DISGUSTING CODE. I GOT SICK OF THIS CHALLENGE SO LETS MOVE ON AND PRETEND THIS NEVER HAPPENED...