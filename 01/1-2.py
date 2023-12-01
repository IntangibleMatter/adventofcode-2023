f = open("./input")

numstr = [
        "zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
        ]
numstr_str = [
        "z0ero", "o1ne", "t2wo", "t3hree", "f4our",
        "f5ive", "s6ix", "s7even", "e8ight", "n9ine"
        ]

nums = []
sum = 0

def firstnum(line):
    index = 0
    num = 0

    for i in range(len(line)):
        if line[i].isdigit():
            index = i
            num = int(line[i])
            break

    for n in range(len(numstr)):
        loc = line.find(numstr[n])
        if loc > -1 and loc < index:
            index = loc
            num = n

    return num


def lastnum(line):
    index = 0
    num = 0

    for i in range(len(line)):
        if line[i].isdigit():
            index = len(line)
            num = int(line[i])

    for n in range(len(numstr)):
        loc = line.rfind(numstr[n])
        if loc > -1 and index < loc:
            index = loc
            num = n

    return num


def line_to_num(line):
    s = ""
    formatted_line = line
    for num in range(len(numstr)):
        formatted_line = formatted_line.replace(numstr[num], numstr_str[num])
    print(formatted_line)

    for l in range(len(formatted_line)):
        if formatted_line[l].isdigit():
            s += formatted_line[l]
        # else:
        #     for item in numstr:
        #         if line[l].find(item, l) == l:
        #             s += numstr.index(item)

    return s


for line in f.readlines():
    # nums.append(str(firstnum(line)) + str(lastnum(line)))
    line_as_num = line_to_num(line)
    nums.append(int(line_as_num[0] + line_as_num[-1]))
    print(line.replace("\n", "") + ' ' + str(nums[-1]))


for n in nums:
    sum += int(n)

print(sum)
