with open('2020\day4.txt', 'r') as f:
    # a list containing all the passports, i.e. strings of lines contained in the file. Each line might have one or multiple key:value pairs or it can even be empty
    passports = [line.strip() for line in f]
# print(passports)

# a set containing the necessary fields for a passport to be valid
required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

# a dictionary containing the field:data or key:value pairs for each passport
passport = dict()

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
            valid += 1
        passport.clear()

# Repeat once more because the file does not contain an empty line in the end, so we are missing the last passport
found_fields_list = passport.keys()
found_fields_set = set(found_fields_list)
found_fields_set.discard('cid')
if found_fields_set == required_fields:
    valid += 1

print(valid)
