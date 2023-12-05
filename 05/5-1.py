f = open("./demoinput")

types = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
         "humidity-to-location"
        ]

seeds = []
# seed to soil
s2s = []
# soild to fertilizer
s2f = []
# fertlizer to water
f2w = []
# water to light
w2l = []
# light to temperature
l2t = []
# temperature to humidity
t2h = []
# humidity to location
h2l = []


locations = []


def arr2int(arr):
    newlist = []
    for item in arr:
        try:
            newlist.append(int(item.strip()))
        except ValueError:
            print("Error when converting", item, "------")

    return newlist


type = ""


def checklinestart(line):
    return "map" in line
    split = line.split(" ")
    for s in split:
        print("--", s, "--")
        if split in types:
            print("found!")
            return True
    return False


for line in f.readlines():
    if line.strip() == "":
        continue
    elif line.startswith("seeds:"):
        seeds = arr2int(line.split(":")[1].split(" "))
        continue
    elif checklinestart(line):
        type = line.split(" ")[0]
    else:
        nums = arr2int(line.split(" "))
        print("appending to", type, ":", nums)
        match type:
            case "seed-to-soil":
                s2s.append(nums)
            case "soil-to-fertilizer":
                s2f.append(nums)
            case "fertilizer-to-water":
                f2w.append(nums)
            case "water-to-light":
                w2l.append(nums)
            case "light-to-temperature":
                l2t.append(nums)
            case "temperature-to-humidity":
                t2h.append(nums)
            case "humidity-to-location":
                h2l.append(nums)


def cmv(value, map):
    for vals in map:
        if value >= vals[1] and value < vals[1] + vals[2]:
            print("found match for ", value, ":", vals[0] + (value - vals[1]))
            return vals[0] + (value - vals[1])
        else:
            continue
    print("no match found, returning", value)
    return value


# reverse of above function
def r_cmv(value, map):
    for vals in map:
        if value >= vals[0] and value < vals[0] + vals[2]:
            #print("found", value, "in range. Mapped to", vals[1])
            return value - vals[0]
        else:
            continue
    return value


for seed in seeds:
    print("Checking seed:", seed)
    locations.append(cmv(cmv(cmv(cmv(cmv(cmv(cmv(seed, s2s), s2f), f2w), w2l), l2t), t2h), h2l))

"""
for l in h2l:
    print("handling", l)
    for i in range(l[0], l[0] + l[2] + 1):
        seed = r_cmv(r_cmv(r_cmv(r_cmv(r_cmv(r_cmv(r_cmv(i, h2l), t2h), l2t), w2l), f2w), s2f), s2s)
        if seed in seeds:
            locations.append(i)
            print("match!")
"""
print(locations)

locations.sort()
print(locations)
