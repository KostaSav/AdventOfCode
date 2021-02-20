with open("2020\day16.txt", "r") as f:
    notes_str = f.read()
#################### Part One ####################
notes_arr = notes_str.split("\n\n")

# Collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby tickets
rules = notes_arr[0].split("\n")
my_ticket = notes_arr[1].replace("\n", "").lstrip("your ticket:")
nearby = notes_arr[2].lstrip("nearby tickets:\n").replace("\n", ",").split(",")

# Get the valid ranges
rules_nums = []
for rule in rules:
    right = rule.split(":")[1]
    ranges = right.split("or")
    rules_nums.append(ranges[0].strip())
    rules_nums.append(ranges[1].strip())
# print(rules_nums)

# Create a set containing all the valid values
allowed = set()
for num in rules_nums:
    low = int(num.split("-")[0])
    high = int(num.split("-")[1])
    for i in range(low, high + 1):
        allowed.add(i)
# print(allowed)

# Chech if each nearby value belongs to the valid set
total = 0
for value in nearby:
    if int(value) not in allowed:
        total += int(value)

print(total)
#################### Part One ####################