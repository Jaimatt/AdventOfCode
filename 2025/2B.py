import math

f = open("2_input.txt")
ranges = f.read().split(",")

# PROCESSING
for x in range(len(ranges)):
    ranges[x] = ranges[x].split("-")
    ranges[x][0] = int(ranges[x][0])
    ranges[x][1] = int(ranges[x][1])

print(ranges)

# STORAGE
invalids = []

factorDict = {
    1: [],
    2: [2],
    3: [3]
    # et cetera. We will calculate more as needed
}

# ALGORITHM
for x in ranges:
    min = x[0]
    max = x[1]
    for y in range(min,max+1):
        string = str(y)
        lenstr = len(string)

        factors = []
        # Check if we know the factors of lenstr
        if lenstr in factorDict:
            factors = factorDict[lenstr]
        else:
            # we will have to calculate them!
            for i in range(2,lenstr+1):
                if lenstr%i == 0:
                    factors.append(i)
            # and store them through memoisation
            factorDict[lenstr] = factors

        # Now, go through each factor of lenstr and see if an appropriate loop exists
        for substringCount in factors:
            substringSize = int(lenstr/substringCount)
            
            substrings = []
            # now loop through the substrings
            for i in range(substringCount):
                substrings.append(string[substringSize*i:substringSize*(i+1)])

            # if there is only one kind of item in this list of substrings, we've found an invalid!
            # just make sure it hasn't already been found
            if len(set(substrings)) == 1 and int(string) not in invalids:
                invalids.append(int(string))

        

print(invalids)
sum = 0
for x in invalids:
    sum = sum + x
print(sum)