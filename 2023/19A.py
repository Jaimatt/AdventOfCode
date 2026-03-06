import time
start = time.time()
i = open('19.txt').read().split('\n\n')

workflows = {x.split('{')[0]:[y for y in x.split('{')[1][:-1].split(',')] for x in i[0].split('\n')}
parts = [{y.split('=')[0]:int(y.split('=')[1]) for y in x[1:-1].split(',')} for x in i[1].split('\n')]

def accepted(part, rules):
    r = rules[0]
    # accept or reject
    if r=='R': return False
    if r=='A': return True

    # other end point
    if ':' not in r: return accepted(part,workflows[r])

    cond, dest = tuple(r.split(':'))
    if '>' in cond and part[cond.split('>')[0]] > int(cond.split('>')[1]):
        return accepted(part,[dest])
    if '<' in cond and part[cond.split('<')[0]] < int(cond.split('<')[1]):
        return accepted(part,[dest])

    return accepted(part,rules[1:])

totals = 0
for p in parts:
    if accepted(p,workflows['in']): totals += sum(p.values())
print(totals)

print("--- %s ms ---" % ((time.time() - start)*1000))