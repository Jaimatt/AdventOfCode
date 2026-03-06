import time
start = time.time()
import sys
i = open('8.txt').read().split('\n\n')
sys.setrecursionlimit(30000) # it actually took like 22,000 levels of recursion. This is unsustainable!

directions = i[0]
graph = {x.split(" = ")[0] : {['L','R'][i]:y for i,y in enumerate(x.split(" = ")[1][1:-1].split(", "))} for x in i[1].split('\n')}

def traverse(node,steps=0):
    if node == 'ZZZ': return(steps)
    return traverse(graph[node][directions[steps%len(directions)]],steps+1)

print(traverse('AAA'))

print("--- %s ms ---" % ((time.time() - start)*1000))