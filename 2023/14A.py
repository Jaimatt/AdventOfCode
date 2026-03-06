import time
start = time.time()
i = open('14.txt').read()

platform = [[y for y in x] for x in i.split('\n')]

def p():
    for row in platform:
        for c in row:
            print(c,end=" ")
        print()
    print()

def val(row,col):
    if not (row in range(len(platform)) and col in range(len(platform[0]))): return '#'
    else: return platform[row][col]

def roll(row,col):
    if val(row-1,col) in ['#','O']: return len(platform) - row
    platform[row][col], platform[row-1][col] = platform[row-1][col], platform[row][col]
    return roll(row-1,col)

total = 0
for r,row in enumerate(platform):
    for c,col in enumerate(row):
        if col == 'O': total += roll(r,c)
print(total)
    
print("--- %s ms ---" % ((time.time() - start)*1000))