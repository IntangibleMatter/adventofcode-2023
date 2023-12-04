f = open("./input")

lines = []

cards = []

for line in f.readlines():
    lines.append(line.split(":")[1])


def toints(li):
    newlist = []
    for el in li:
        if not el == "":
            newlist.append(int(el))

    return newlist


for line in lines:
    print(line)
    winningnums = []
    hasnums = []
    score = 0

    splitline = line.split("|")

    winningnums = toints(splitline[0].split(" "))
    hasnums = toints(splitline[1].split(" "))

    # matchcount = len([n for n in hasnums if n in winningnums])
    matchcount = 0

    print("has", hasnums)
    print("winning", winningnums)

    for n in hasnums:
        if n in winningnums:
            matchcount += 1

    print("matches", matchcount)

    if matchcount <= 2:
        score = matchcount
        cards.append(score)
        print(score)
    else:
        score = pow(2, (matchcount - 1))
        cards.append(score)
        print(score)


sum = 0

for n in cards:
    sum += n

print(sum)
