f = open("./demoinput")

hands = []

order = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]

# handtypes = ["hc", "1p", "2p", "3k", "fh", "4k", "5k"]

# I fucking hate python's lack of Enums.
T_HC = 0
T_1P = 1
T_2P = 2
T_3K = 3
T_FH = 4
T_4K = 5
T_5K = 6
handgroups = [[], [], [], [], [], [], []]

for line in f.readlines():
    hands.append(line.strip().split(" "))


def parsetype(hand):
    counts = []
    for h in order:
        counts.append(hand.count(h))

    counts.sort(reverse=True)

    match counts[0]:
        case 1:  # high card
            return T_HC
        case 2:  # pair, either 1 or 2
            match counts[1]:
                case 2:  # 2 pair
                    return T_2P
                case _:  # one pair
                    return T_1P
        case 3:
            match counts[1]:
                case 2:  # Full house
                    return T_FH
                case _:  # 3 of a kind
                    return T_3K
        case 4:  # 4 of a kind
            return T_4K
        case 5:  # 5 of a kind
            return T_5K
        case _:
            return -1

for hand in hands:
    htype = parsetype(hand[0])
    if htype < 0:
        print("yo what the fuck?", hand, "ran into some issues when being parsed.")
    handgroups[htype].append(hand)
