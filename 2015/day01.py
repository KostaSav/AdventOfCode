# Read the txt file and assign to a string variable
with open("2015\day01.txt", "r") as f:
    entries_str = f.read()

# ------ Part One ------ #

# Count the parentheses
up = entries_str.count("(")
down = entries_str.count(")")

# Calculate the floor
floor = up - down
print(floor)

# ------ End of Part One ------ #


# ------ Part Two ------ #

# Iterate the whole file until reaching floor -1
up = down = 0
for i in range(len(entries_str)):
    if entries_str[i] == "(":
        up += 1
    else:
        down += 1
    if (up - down) == -1:
        print("Position is " + str(i + 1) + ".")
        break

# ------ End of Part Two ------ #