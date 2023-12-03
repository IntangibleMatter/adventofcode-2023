# import time
f = open("./input")

lines = []

ints = []

for line in f.readlines():
    lines.append(line)


def check_num_run(line: int, char: int):
    start = char
    end = char

    print(lines[line][start])
    if start - 1 > 0:
        if lines[line][start - 1].isdigit():
            while lines[line][start].isdigit():
                if start - 1 >= 0:
                    if lines[line][start - 1].isdigit():
                        start -= 1
                    else:
                        break
                else:
                    break
        else:
            print("start of number already selected")

    print("start", start)

    print(lines[line][end])
    if end + 1 < len(lines[line]):
        if lines[line][end + 1].isdigit():
            print("more to find")
            while lines[line][end].isdigit():
                # time.sleep(0.1)
                print("e", end)
                if end + 1 <= len(lines[line]):
                    if lines[line][end + 1].isdigit():
                        end += 1
                    else:
                        break
                else:
                    break
        else:
            print("wghwhwhhw")

    print("end", end)
    print("n : (", lines[line][start:end + 1], ")")
    return int(lines[line][start:end + 1]), (start, end)


def check_if_num_seen(char, ranges):
    for r in ranges:
        if char >= r[0] and char <= r[1]:
            return True

    return False


def check_char_adjacencies(line: int, char: int):
    nums = []
    covered_ranges = []
    for i in range(-1, 2):
        covered_ranges.clear()
        if line + i > len(lines) or line + i < 0:
            print("skipping ", line + i)
            continue
        for j in range(-1, 2):
            if check_if_num_seen(char + j, covered_ranges):
                print("num covered ", char + j)
                continue
            if char + j > len(lines[line]) or char + j < 0:
                print("skipping char ", char + j)
                continue

            if lines[line + i][char + j].isdigit():
                result = check_num_run(line + i, char + j)
                nums.append(result[0])
                covered_ranges.append(result[1])

    if len(nums) == 2:
        ints.append(nums[0] * nums[1])


def check_line_adjacencies(line: int):
    char = 0
    while char < len(lines[line]):
        if lines[line][char] == "*":
            check_char_adjacencies(line, char)

        char += 1


for line in range(len(lines)):
    check_line_adjacencies(line)


sum = 0
for i in ints:
    sum += i

print(sum)
