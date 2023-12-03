f = open("./input")

lines: list = []
symbols: list = [
        "!", "@", "#", "$", "%", "^", "&", "*",
        "(", ")", "`", "~", "[", "]", "\\", "|",
        ";", ":", "'", '"', ",", "<", ">", "/",
        "?", "-", "_", "=", "+"
        ]

ints: list = []

for line in f.readlines():
    lines.append(line)


def check_chars_next_to_num(line: int, num_index: int):
    print("checking num char {}".format(lines[line][num_index]))
    for i in range(-1, 2):
        print("-checking line {}".format(line + i))
        if not (line + i < len(lines) and line + i >= 0):
            print("skipped line {}".format(line + i))
            continue
        print("line: {}".format(lines[line + i]))
        for j in range(-1, 2):
            print("-checking char {}".format(num_index + j))
            if num_index + j < 0 or num_index + j >= len(lines[line]):
                print("skipped char {}".format(num_index + j))
                continue
            print("char: {}".format(lines[line+i][num_index + j]))

            if lines[line + i][num_index + j] in symbols:
                print("found symbol: {}".format(lines[line + i][num_index + j]))
                return True
    return False


def check_num_adjacencies(line: int, num_start: int):
    num_end: int = 1
    for i in range(num_start, len(lines[line])):
        if not lines[line][i].isdigit():
            num_end = i
            break

    for i in range(num_start, num_end):
        print("checking num: %s" % lines[line][num_start:num_end])
        if check_chars_next_to_num(line, i):
            print("num: {}".format(lines[line][num_start:num_end]))
            ints.append(int(lines[line][num_start:num_end]))
            break

    # we just need to know where the number ends so we can do the next one
    return num_end


def check_for_adjacencies(line: int):
    char = 0
    while char < len(lines[line]):
        if lines[line][char].isdigit():
            num_end = check_num_adjacencies(line, char)
            char = num_end
            continue

        char += 1

for line in range(len(lines)):
    print("running line: %d" % line)
    check_for_adjacencies(line)

print(len(lines))
sum = 0
for n in ints:
    sum += n

print(sum)
