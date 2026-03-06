f = open("3_input.txt")
banks = f.read().split("\n")

sum=0

for bank in banks:
    searchStart = [-1]
    for num in range(12):
        # search through the appropriate entries in the bank
        maxIndex = searchStart[num]+1
        # find the index of the largest number for the lead digit
        for digitIndex in range(searchStart[num]+1,len(bank)-(12-num)+1):
            if bank[digitIndex] > bank[maxIndex]:
                maxIndex = digitIndex
        # now, set this index as the starting point for the next search
        searchStart.append(maxIndex)
    # now we have the indexes of the 'largest' elements within their appropriate regions. These are the indexes of the digits on the max values
    # Use them to calculate teh joltage

    joltage = 0
    for digit in range(1,13):
        joltage = joltage + int(bank[searchStart[digit]])*(10**(12-digit))
    # print(joltage)
    sum = sum + joltage

print(sum)