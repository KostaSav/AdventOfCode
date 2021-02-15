import math

with open("2020\day13.txt", "r") as f:
    notes = [line.strip() for line in f]

# print(notes)


#################### Part One ####################
timestamp_earliest = int(notes[0])
ids = notes[1].split(",")

timestamp_final = timestamp_earliest
earliest_bus = 0

# print(earliest)
# print(ids)

found = False

while not found:
    for id in ids:
        if id == "x":
            continue
        elif timestamp_final % int(id) == 0:
            found = True
            earliest_bus = int(id)
            break
        elif id == ids[len(ids) - 1]:
            timestamp_final += 1
            break

# print(earliest_bus)
# print(earliest_bus * (timestamp_final - timestamp_earliest))
#################### Part One ####################



#################### Part Two ####################
## Could not find out how to increase the number of steps (named "offset" in the code) each time two bus IDs are "synced", so I followed Bradley Sward's solution:
## https://www.youtube.com/watch?v=4115vd8-yeY
## using the math.lcm() function from Python 3.9 (https://docs.python.org/3.9/library/math.html#math.lcm)
ids_dict = {}

for i in range(len(ids)):
    if ids[i] == "x":
        continue
    else:
        ids_dict.update({int(ids[i]): i})

# print(ids_dict)
ids_dict_sorted = sorted(ids_dict.items())
# print(ids_dict_sorted)
# print(*ids_dict_sorted[:2])
# print(*sorted(ids_dict.keys())[:2])


timestamp_final = 0
offset = 1
for i in range(1, len(ids_dict_sorted)):
    found_2 = False
    while not found_2:
        found_2 = True  # not realy found, but will turn to False as soon as we don't have a match and need to iterate forwards
        for j in range(0, i + 1):
            if (timestamp_final + ids_dict_sorted[j][1]) % ids_dict_sorted[j][0] != 0:
                found_2 = False
                break
        if found_2 == True:  # if our flag remained unchanged, we really found a match
            offset = math.lcm(*sorted(ids_dict.keys())[:j])
            print("Found a new one at: " + str(timestamp_final))
            break
        else:
            timestamp_final += offset

print(timestamp_final)
#################### Part Two ####################