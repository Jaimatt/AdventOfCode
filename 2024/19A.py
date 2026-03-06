m = open('19.txt').read()

towels = [x for x in m.split('\n')[0].split(', ')]
patterns = [x for x in m.split('\n')[2:]]

def isPossible(pattern):
    # base: empty towel
    if pattern == '':
        return True
    
    # recurse: test all towels
    for towel in towels:
        lentowel = len(towel)
        if towel == pattern[:lentowel]:
            if isPossible(pattern[lentowel:]): return True
        
    return False

count = 0
for p in patterns:
    count += isPossible(p)
print(count)