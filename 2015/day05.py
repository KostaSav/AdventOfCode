with open("2015/day05.txt", "r") as f:
    strings_arr = [line.strip() for line in f]

# ------ Part One ------ #

nice = 0

for string in strings_arr:
    if any(substring in string for substring in ["ab", "cd", "pq", "xy"]):
        continue
    elif (
        string.count("a")
        + string.count("e")
        + string.count("i")
        + string.count("o")
        + string.count("u")
        > 2
    ) and any(string[i] == string[i - 1] for i in range(1, len(string))):
        nice += 1
        continue

print(nice)

# ------ End of Part One ------ #


# ------ Part Two ------ #

nice_2 = 0

for string in strings_arr:
    substrings_arr_2 = [string[i - 1: i + 1] for i in range(1, len(string))]
    substrings_arr_3 = [string[i - 2: i + 1] for i in range(2, len(string))]
    if any(
        substring[0] == substring[2]
        for substring in substrings_arr_3
    ):
        for sub in substrings_arr_2:
            if string.count(sub) > 1:
                nice_2 += 1
                break

print(nice_2)

# ------ End of Part Two ------ #
