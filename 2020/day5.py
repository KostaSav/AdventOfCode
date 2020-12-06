import math

with open('2020\day5.txt', 'r') as f:
    bpasses = [line.strip() for line in f]

# print(bpasses)

max_bpass = 0
ids = set()


for bpass in bpasses:
    front = 0
    back = 127
    lower = 0
    upper = 7

    for i in range(7):
        if bpass[i] == "F":
            back = math.floor((back+front)/2)
        else:
            front = math.ceil((back+front)/2)
    # print(str(front) + "-" + str(back))

    for j in range(7, 10):
        if bpass[j] == "L":
            upper = math.floor((lower+upper)/2)
        else:
            lower = math.ceil((lower+upper)/2)

    id = back*8 + upper
    ids.add(id)
    if id > max_bpass:
        max_bpass = back*8 + upper

print(max_bpass)

# Part Two
for i in range(max_bpass):
    if i not in ids and i-1 in ids and i+1 in ids:
        print(i)
