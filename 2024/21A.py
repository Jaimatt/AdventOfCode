keycodes = open('21.txt').read().split("\n")

def sign(x):
    return -1 if x < 0 else (1 if x > 0 else 0)

def findInGrid(grid,item):
    for y,row in enumerate(grid):
        for x,col in enumerate(row):
            if col == item: return x,y

def buttonPresser(grid,code):
    x,y = findInGrid(grid,'A')
    output = ""

    for c in code:
        endx,endy = findInGrid(grid,c)
        u = '^' if sign(y-endy)>0 else 'v'
        s = '<' if sign(x-endx)>0 else '>'

        ud = u * abs(y-endy)
        lr = s * abs(x-endx)

        gapx,gapy = findInGrid(grid,' ')

        # These conditions are stolen from the web
        # If Moving right and there's no gap at the (.) then it's safe to go vertically first (ideal)
        # 
        #   A >>  
        #     
        #   .      B
        if endx > x and [endy,x] != [gapy,gapx]:
            output += ud + lr + "A"
        # Otherwise, so long as there's no gap at the dot, do horizontal first
        # 
        #   A  >>> .
        #          v
        #          B
        elif [y,endx] != [gapy,gapx]:
            output += lr + ud + "A"
        # Of couse if there is a gap there, then there's no gap blocking the vertical path. So do that.
        else:
            output += ud + lr + "A"

        # This works because... reasons I guess
            
        x,y = endx,endy
    
    return output

numGrid = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    [' ','0','A']
]
arrowGrid = [
    [' ','^','A'],
    ['<','v','>']
]

total = 0
for keycode in keycodes:
    first = buttonPresser(numGrid,keycode)
    second = buttonPresser(arrowGrid,first)
    third = buttonPresser(arrowGrid,second)
    total += len(third) * int(keycode[:-1])
    print(len(third),int(keycode[:-1]))
print(total)