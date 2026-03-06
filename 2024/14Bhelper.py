# by inspection, the horizontal aligned into a patter at
# n=38 and n=139 (i.e. every 101 multiple after n=38)

# and the vertical at n=88 and, presumably, n=191

# so find the point where they'll intercept!

horiz = []

vert = []

for x in range(1000):
    horiz.append(38 + 101*x)
    vert.append(88 + 103*x)

inter = set(horiz).intersection(set(vert))

print(min(inter))
# --> 7916