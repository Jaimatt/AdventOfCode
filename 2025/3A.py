f = open("3_input.txt")
banks = f.read().split("\n")

print(banks)

sum=0

for bank in banks:
    # the first digit will be in this region 0 to len-1
    maxIndex = 0
    for digitIndex in range(len(bank)-1):
        if bank[digitIndex] > bank[maxIndex]:
            maxIndex = digitIndex
    
    # now the first digit is the max
    firstDigit = bank[maxIndex]

    # the second digit will be after the max index
    secondIndex = maxIndex+1
    for digitIndex in range(maxIndex+1,len(bank)):
        if bank[digitIndex] > bank[secondIndex]:
            secondIndex = digitIndex
    secondDigit = bank[secondIndex]

    joltage = int(firstDigit)*10 + int(secondDigit)
    print(joltage)
    sum = sum + joltage

print(sum)