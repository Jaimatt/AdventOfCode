import time
start = time.time()
i = open('14_test.txt').read()

platform = [[y for y in x] for x in i.split('\n')]

def p():
    for row in platform:
        for c in row:
            print(c,end=" ")
        print()
    print()

def val(row,col):
    if not (row in range(len(platform)) and col in range(len(platform[0]))): return '#'
    return platform[row][col]

def roll(row,col,dr,dc):
    if val(row+dr,col+dc) == '#': return
    if val(row+dr,col+dc) == '.':
        platform[row][col] = '.'
        platform[row+dr][col+dc] = 'O'
    roll(row+dr,col+dc,dr,dc)

def tilt(dr,dc):
    for r,row in enumerate(platform):
        for c,col in enumerate(row):
            if col == 'O': roll(r,c,dr,dc)


p()
tilt(-1,0)
p()
tilt(0,-1)
p()
tilt(1,0)
p()
tilt(0,1)
p()
    
print("--- %s ms ---" % ((time.time() - start)*1000))