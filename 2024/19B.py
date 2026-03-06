import time
ti = time.time()

m = open('19.txt').read()

towels = [x for x in m.split('\n')[0].split(', ')]
patterns = [x for x in m.split('\n')[2:]]

memos = {}

def numPossible(pattern):
    # base: empty towel
    if pattern == '':
        return 1
    
    # get memo
    if pattern in memos: return memos[pattern]
        
    # recurse: test all towels
    num = 0
    for towel in towels:
        lentowel = len(towel)
        if towel == pattern[:lentowel]:
            num += numPossible(pattern[lentowel:])

    # save memo
    memos[pattern] = num

    return num

total = 0
for k, p in enumerate(patterns):
    n = numPossible(p)
    total += n
print(total)

print(str(time.time() - ti) + " seconds")