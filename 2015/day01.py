"""
--- Day 1: Not Quite Lisp ---
"""

# Read the txt file and assign to a string variable
with open("2015/day01.txt", "r", encoding="utf-8") as f:
    entries_str = f.read()

# ------ Part One ------ #

# Count the parentheses
UP = entries_str.count("(")
DOWN = entries_str.count(")")

# Calculate the floor
floor = UP - DOWN
print(floor)

# ------ End of Part One ------ #


# ------ Part Two ------ #

# Iterate the whole file until reaching floor -1
UP = DOWN = 0
for i in range(len(entries_str)):
    if entries_str[i] == "(":
        UP += 1
    else:
        DOWN += 1
    if (UP - DOWN) == -1:
        print("Position is " + str(i + 1) + ".")
        break

# ------ End of Part Two ------ #
