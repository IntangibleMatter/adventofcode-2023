import re
f = open("./input")

games = {}

def parsecubes1(line):
    id = line.split(":")[0].replace("Game ", "").strip()

    game = line.split(";")
    game[0] = re.sub(r"Game %d:", "", game[0])

    cubes = {"r": 0, "g": 0, "b": 0}

    for subgame in game:
        cubeset = subgame.split(", ")
        for cube in cubeset:
            c = cube.split(" ")
            match c[1].strip():
                case "red":
                    cubes["r"] = cubes["r"] + int(c[0])
                case "green":
                    cubes["g"] = cubes["g"] + int(c[0])
                case "blue":
                    cubes["b"] = cubes["b"] + int(c[0])

    games[id] = cubes


def parsecubes2(line):
    firstsplit = line.split(":")
    id = firstsplit[0].replace("Game ", "").strip()

    linegame = firstsplit[1].split(";")

    linegames = []

    for game in linegame:
        cubesplit = game.split(", ")
        cubes = {"r": 0, "g": 0, "b": 0}
        for cube in cubesplit:
            if "red" in cube:
                cubes["r"] = cubes["r"] + int(re.sub(r"\D", "", cube))
            elif "green" in cube:
                cubes["g"] = cubes["g"] + int(re.sub(r"\D", "", cube))
            elif "blue" in cube:
                cubes["b"] = cubes["b"] + int(re.sub(r"\D", "", cube))
        linegames.append(cubes)
    """
    sums = {"r": 0, "g": 0, "b": 0}
    for game in linegames:
        sums["r"] += game["r"]
        sums["g"] += game["g"]
        sums["b"] += game["b"]
    """
    game_valid = True

    for game in linegames:
        if game["r"] <= 12 and game["g"] <= 13 and game["b"] <= 14:
            game_valid = True
        else:
            game_valid = False
            break

    games[id] = game_valid



for line in f.readlines():
    parsecubes2(line)


f.close()

sum = 0

for game in games:
    print("{} --- {}".format(game, games[game]))
    if games[game]:
        sum += int(game)
    """
    if games[game]["r"] <= 12 and games[game]["g"] <= 13 and games[game]["b"] <= 14:
        sum += int(game)
        print("---- valid ----")
    """
print(sum)
