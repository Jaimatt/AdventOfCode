import time
from functools import cmp_to_key
start = time.time()
i = open('7.txt').read()

cards = [[x.split(" ")[0],int(x.split(" ")[1])] for x in i.split("\n")]
values = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def type(card):
    if card.count(card[0]) == 5: return 6 # five of a kind
    if card.count(card[0]) == 4 or card.count(card[1]) == 4: return 5 # four of a kind
    if len(set([x for x in card])) == 2: return 4 # full house
    if card.count(card[0]) == 3 or card.count(card[1]) == 3 or card.count(card[2]) == 3 : return 3 # three of a kind
    if len(set([x for x in card])) == 3: return 2 # two pair
    if len(set([x for x in card])) == 4: return 1 # one pair
    return 0 #high card

def compareCards(a,b):
    diff = type(a[0]) - type(b[0])
    if diff: return diff
    for i in range(5):
        if a[0][i] == b[0][i]: continue
        return values.index(a[0][i]) - values.index(b[0][i])
    return 0

cards.sort(key=cmp_to_key(compareCards))
winnings = 0
for i, c in enumerate(cards):
    winnings += (i+1) * c[1]
print(winnings)

print("--- %s ms ---" % ((time.time() - start)*1000))