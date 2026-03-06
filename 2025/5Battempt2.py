# define the sorting function
def sortByMin(r):
    return r[0]

# read and process data
f = open("5_input.txt")
data = f.read().split("\n\n")

ranges = data[0].split("\n")

for x in range(len(ranges)):
    ranges[x] = ranges[x].split("-")
    ranges[x][0] = int(ranges[x][0])
    ranges[x][1] = int(ranges[x][1])

# set up variables
intervals = []
inMin = 0
inMax = 0
validIDs = 0

# sort data
ranges.sort(key=sortByMin)

# go through each range, constructing intervals
for r in ranges:
    # if the minimum of the range exceeds the existing maximum of the interval, end the interval now, save it and start a new one
    if r[0] > inMax:
        intervals.append([inMin,inMax])
        inMin = r[0]
        inMax = r[0]

    # otherwise, this new range is contained in our constructed interval, which we may choose to extend to the lenght of this current range
    if r[1] > inMax:
        inMax = r[1]
# save the last interval
intervals.append([inMin,inMax])

# count the length of each interval
for i in intervals:
    validIDs += i[1]-i[0]+1

# remove the null interval
validIDs += -1

# print the results
print(intervals)
print(validIDs)
