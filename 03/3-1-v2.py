import re

f = open("./demoinput")

lines = []
adjacencies = []

nums = []

nonnum = re.compile(r"[^\d\.\n]")

for line in f.readlines():
    lines.append(line)

for line in range(len(lines)):
    for char in range(len(lines[line])):
        charcount = 0
        for i in range(-1, 2):
            if i < 0 or line + i >= len(lines):
                continue
            for j in range(-1, 2):
                if j < 0 or char + j >= len(lines[line]):
                    continue
                print(lines[line + i][char + j])
                if nonnum.match(lines[line + i][char + j]):
                    print("match: ", lines[line + i][char + j])
                    charcount += 1
print(adjacencies)
print(lines)

for line in range(len(lines)):
    char = 0
    while char < len(lines[line]):
        if not lines[line][char].isdigit():
            char += 1
            continue

        num_counts = False
        c = char
        while lines[line][c].isdigit():
            if int(adjacencies[line][c]) > 0:
                num_counts = True
            c += 1
            if c > len(lines[line]):
                break
            elif not lines[line][c].isdigit():
                break

        nums.append(int(lines[line][char:c]))

sum = 0
for n in nums:
    sum += n

print(sum)
