f = open("6_input.txt")
data = f.read().split("\n")

def colEmpty(i):
    for row in range(len(data)):
        if data[row][i] != ' ':
            return False
    return True

def getNumAt(c):
    out = ""
    for row in range(len(data)-1):
        out += data[row][c]
    return int(out)

operation = '+'
total = 0
result = 0

for column in range(len(data[0])):
    # if this is the end of a calculation, save the information
    if colEmpty(column):
        total += result
        # print('empty')
        continue
    # else:
        # print('not empty')

    # if this is the start of a calculation, reset the result counter
    if data[len(data)-1][column] != ' ':
        operation = data[len(data)-1][column]
        # print([operation])
        if operation == '+':
            result = 0
        if operation == '*':
            result = 1

    # now, just add the new number
    num = getNumAt(column)

    if operation == '+':
        result += num
    if operation == '*':
        result = result * num


print(total)