"""
--- Day 2: I Was Told There Would Be No Math ---
"""

with open("2015/day02.txt", "r", encoding="utf-8") as f:
    entries_arr = [line.strip() for line in f]

# ------ Part One ------ #
TOTAL = 0

for entry in entries_arr:
    l = int(entry.split("x")[0])
    w = int(entry.split("x")[1])
    h = int(entry.split("x")[2])
    surface_1 = l * w
    surface_2 = w * h
    surface_3 = h * l
    small_side = min(surface_1, surface_2, surface_3)
    paper = 2 * surface_1 + 2 * surface_2 + 2 * surface_3 + small_side
    TOTAL += paper

print(TOTAL)

# ------ End of Part One ------ #


# ------ Part Two ------ #
TOTAL_RIBBON = 0

for entry in entries_arr:
    l = int(entry.split("x")[0])
    w = int(entry.split("x")[1])
    h = int(entry.split("x")[2])
    sides = [l, w, h]

    smallest_first = min(sides)
    sides.remove(smallest_first)
    smallest_second = min(sides)

    bow = l * w * h

    ribbon = 2 * smallest_first + 2 * smallest_second + bow
    TOTAL_RIBBON += ribbon

print(TOTAL_RIBBON)

# ------ End of Part Two ------ #
