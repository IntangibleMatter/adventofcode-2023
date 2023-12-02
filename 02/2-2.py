import re
f = open("./input")

games = {}

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
    max_count = {"r": 0, "g": 0, "b": 0}
    for game in linegames:
        if game["r"] > max_count["r"]:
            max_count["r"] = game["r"]
        if game["g"] > max_count["g"]:
            max_count["g"] = game["g"]
        if game["b"] > max_count["b"]:
            max_count["b"] = game["b"]

    games[id] = max_count["r"] * max_count["g"] * max_count["b"]


for line in f.readlines():
    parsecubes2(line)


sum = 0

for game in games:
    sum += games[game]

print(sum)
