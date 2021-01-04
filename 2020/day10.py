with open('2020\day10.txt', 'r') as f:
    adapters = [int(line.strip()) for line in f]

# print(adapters)

#################### Part One ####################
one_jolt_diffs = 0
three_jolt_diffs = 0

# Sort the adapters array to avoid too much work!
adapters_sorted = sorted(adapters)

# print(adapters_sorted)

# The charging outlet near our seat has an effective joltage of 0,
# so the first difference is between the wall and the smallest adapter
if adapters_sorted[0] == 1:
    one_jolt_diffs += 1
elif adapters_sorted[0] == 3:
    three_jolt_diffs += 1

# Calculate the differences for the rest of our adapters
for i in range(1, len(adapters_sorted)):
    diff = adapters_sorted[i] - adapters_sorted[i-1]
    if diff == 1:
        one_jolt_diffs += 1
    elif diff == 3:
        three_jolt_diffs += 1

# Add a final difference of +3 for the device's built-in adapter
three_jolt_diffs += 1

# Multiply the product of the differences
product = one_jolt_diffs * three_jolt_diffs
print(product)
print()

#################### Part One ####################


#################### Part Two ####################
# Once again I had to resort to help...
# Bradley Sward's solution:
# https://www.youtube.com/watch?v=eeYanhLamjg
# (not even sure I fully grasp it, will recheck later)
adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()

paths = [0] * (max(adapters) + 1)
paths[0] = 1
# print(paths)

for index in range(1, max(adapters)+1):
    for x in range(1, 4):
        if (index - x) in adapters:
            paths[index] += paths[index-x]
    # print(paths)

print(paths[-1])
#################### Part Two ####################
