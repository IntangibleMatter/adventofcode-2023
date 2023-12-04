import time as t

f = open("./input")

cards = []
cardcount = 0

lines = []

totalcards = 0

seencards = []

for line in f.readlines():
    lines.append(line.strip())


def toints(li):
    newlist = []
    for el in li:
        if not el == "":
            newlist.append(int(el))

    return newlist


def checkmatches(card: dict):
    matchcount = 0
    for n in card["has"]:
        if n in card["winning"]:
            matchcount += 1
    return matchcount


for line in range(len(lines)):
    card = {"winning": [], "has": [], "copies": []}
    carddat = lines[line].split(":")[1].split("|")
    card["winning"] = toints(carddat[0].split(" "))
    card["has"] = toints(carddat[1].split(" "))

    copycount = checkmatches(card)

    copies = []
    for n in range(copycount):
        if line + n < len(lines) + 1:
            copies.append(line + n)

    card["copies"] = copies
    cards.append(card)

seencards = [1] * len(cards)

"""
def instancecards(cad, totalcards):
    totalcards += 1
    for c in card["copies"]:
        if c < len(cards):
            instancecards(cards[c], totalcards)


print(cards)
for card in cards:
    print(card)
    instancecards(card, totalcards)
"""
print(cards)

for card in range(len(cards)):
    t.sleep(0.0001)
    print("card:", cards[card], "iterating:", seencards[card])
    for i in range(seencards[card]):
        print("iteration", i)
        t.sleep(0.0001)
        for c in cards[card]["copies"]:
            t.sleep(0.0001)
            print("incrementing:", c)
            seencards[c] += 1

sum = 0
for n in seencards:
    sum += n

print(sum)
