import math

f = open("6_input.txt")
data = f.read().split("\n")

# CREATE THE ARRAY

fixedData = []

for arr in range(len(data)):
    row = data[arr].split(" ")
    row = [x for x in row if x.strip()]
    fixedData.append(row)

print(fixedData)

# CALCULATE THE ANSWER

total = 0

for column in range(len(fixedData[0])):
    operation = fixedData[len(fixedData)-1][column]
    result = 1
    if operation == '+':
        result = 0
    
    for row in range(len(fixedData)-1):
        val = int(fixedData[row][column])
        if operation == '+':
            result += val
        if operation == '*':
            result = result * val
    print(result)
    total += result

print(total)