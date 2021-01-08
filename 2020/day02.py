with open('day2.txt', 'r') as f:
    database = [line.strip() for line in f]


#################### Part 1 ####################
def is_valid_part_1(lowest, highest, letter, password):
    value = password.count(letter)
    if lowest <= value <= highest:
        return True
    else:
        return False
#################### Part 1 ####################


#################### Part 2 ####################
def is_valid_part_2(first, second, letter, password):
    if (password[first-1] == letter and password[second-1] == letter) or (password[first-1] != letter and password[second-1] != letter):
        return False
    else:
        return True
#################### Part 2 ####################


countValidPart1 = 0
countValidPart2 = 0

for entry in database:
    separated = entry.split()
    lowest = int(separated[0].split("-")[0])
    highest = int(separated[0].split("-")[1])
    letter = separated[1].split(":")[0]
    password = separated[2]
    if(is_valid_part_1(lowest, highest, letter, password)):
        countValidPart1 += 1
    if(is_valid_part_2(lowest, highest, letter, password)):
        countValidPart2 += 1

print(countValidPart1)
print(countValidPart2)
