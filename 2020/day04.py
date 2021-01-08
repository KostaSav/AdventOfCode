with open('2020\day4.txt', 'r') as f:
    # a list containing all the passports, i.e. strings of lines contained in the file. Each line might have one or multiple key:value pairs or it can even be empty
    passports = [line.strip() for line in f]
# print(passports)

# a set containing the necessary fields for a passport to be valid
required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

# a dictionary containing the field:data or key:value pairs for each passport
passport = dict()


# Part Two method to validate passports with strict rules
def validate(passport):
    if not (len(passport["byr"]) == 4 and int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002):
        # print("byr")
        return False

    if not (len(passport["iyr"]) == 4 and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020):
        # print("iyr")
        return False

    if not (len(passport["eyr"]) == 4 and int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030):
        # print("eyr")
        return False

    if not (passport["hgt"].endswith("cm") or passport["hgt"].endswith("in")):
        # print("hgt")
        return False
    elif passport["hgt"].endswith("cm"):
        if not (int(passport["hgt"].rstrip("cm")) >= 150 and int(passport["hgt"].rstrip("cm")) <= 193):
            # print("hgt cm")
            return False
    elif passport["hgt"].endswith("in"):
        if not (int(passport["hgt"].rstrip("in")) >= 59 and int(passport["hgt"].rstrip("in")) <= 76):
            # print("hgt in")
            return False

    if not (len(passport["hcl"]) == 7 and passport["hcl"].startswith("#") and passport["hcl"].lstrip("#").isalnum()):
        # print("hcl")
        return False

    if not (passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        # print("ecl")
        return False

    if not (len(passport["pid"]) == 9 and passport["pid"].isdecimal()):
        # print("pid")
        return False

    return True


# a counter for valid passports
valid = 0

# Iterate the passports array and add entries to a passport dictionary, until we find an empty line. Then, we clear the passport dictionary and start iterating again
for line in passports:
    if len(line) > 0:
        line = line.split()
        for entry in line:
            passport.update({entry.split(":")[0]: entry.split(":")[1]})
    else:
        found_fields_list = passport.keys()
        found_fields_set = set(found_fields_list)
        found_fields_set.discard('cid')
        if found_fields_set == required_fields:
            if validate(passport):  # Part Two
                valid += 1
        passport.clear()

# Repeat once more because the file does not contain an empty line in the end, so we are missing the last passport
found_fields_list = passport.keys()
found_fields_set = set(found_fields_list)
found_fields_set.discard('cid')
if found_fields_set == required_fields:
    if validate(passport):  # Part Two
        valid += 1

print(valid)
