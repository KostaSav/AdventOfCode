"""
Day 6: Probably a Fire Hazard
"""

with open("2015/day06.txt", "r", encoding="utf-8") as f:
    instructions_arr = [line.strip() for line in f]

# ------------------ Part One ------------------ #

grid = [[0 for x in range(1000)] for y in range(1000)]
LIT = 0

for instr in instructions_arr:
    if "on" in instr:
        KEYWORD = "on"
    elif "off" in instr:
        KEYWORD = "off"
    else:
        KEYWORD = "toggle"

    x_start = int(instr[instr.index(KEYWORD) + len(KEYWORD) + 1 : instr.index(",")])
    y_start = int(instr[instr.index(",") + 1 : instr.index("through")])

    x_end = int(
        instr[instr.index("through") + 8 : instr.index(",", instr.index("through"))]
    )
    y_end = int(instr[instr.index(",", instr.index("through")) + 1 :])

    # print(str(x_start) + "-" + str(y_start) + " || " + str(x_end) + "-" + str(y_end))

    if KEYWORD != "toggle":
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                if KEYWORD == "on":
                    LIT = LIT + 1 if grid[x][y] == 0 else LIT
                    grid[x][y] = 1
                else:
                    LIT = LIT - 1 if grid[x][y] == 1 else LIT
                    grid[x][y] = 0
    else:
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                grid[x][y] = 1 if grid[x][y] == 0 else 0
                LIT = LIT + 1 if grid[x][y] == 1 else LIT - 1

print(LIT)

# ------------------ End of Part One ------------------ #


# ------------------ Part Two ------------------ #

grid = [[0 for x in range(1000)] for y in range(1000)]
LIT = 0

for instr in instructions_arr:
    if "on" in instr:
        KEYWORD = "on"
    elif "off" in instr:
        KEYWORD = "off"
    else:
        KEYWORD = "toggle"

    x_start = int(instr[instr.index(KEYWORD) + len(KEYWORD) + 1 : instr.index(",")])
    y_start = int(instr[instr.index(",") + 1 : instr.index("through")])

    x_end = int(
        instr[instr.index("through") + 8 : instr.index(",", instr.index("through"))]
    )
    y_end = int(instr[instr.index(",", instr.index("through")) + 1 :])

    # print(str(x_start) + "-" + str(y_start) + " || " + str(x_end) + "-" + str(y_end))

    if KEYWORD != "toggle":
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                if KEYWORD == "on":
                    LIT = LIT + 1
                    grid[x][y] += 1
                else:
                    LIT = LIT - 1 if grid[x][y] > 0 else LIT
                    grid[x][y] = grid[x][y] - 1 if grid[x][y] > 0 else grid[x][y]
    else:
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                grid[x][y] += 2
                LIT += 2

print(LIT)

# ------------------ End of Part TWo ------------------ #
