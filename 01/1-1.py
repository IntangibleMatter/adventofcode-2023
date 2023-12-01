import re

f = open("./input")
lines = f.readlines()
f.close()

nums = []

for line in lines:
    lt = re.sub(r'\D+', '', line)

    if len(lt) == 0:
        print("empty line")
    else:
        nl = lt[0] + lt[-1]
        nums.append(int(nl))
    print(lt)
    print(nums[-1])


sum = 0
for i in nums:
    sum += i

print(sum)
