with open('2020\day7.txt', 'r') as f:
    rules = [line.strip() for line in f]

# print(rules)

#################### Part One ####################
rules_dict = dict()

for rule in rules:
    # print(rule)
    keyBag = rule.split("contain")[0].replace("bags", "").strip()
    # print(keyBag + ":")
    contents_str = rule.split("contain")[1]
    contents_arr = contents_str.split(",")
    for i in range(len(contents_arr)):
        contents_arr[i] = contents_arr[i].lstrip("123456789 ").rstrip(
            ".").replace("bags", "").replace("bag", "").strip()
    # print(type(contents_arr))

    rules_dict.update({keyBag: contents_arr})


# for key, value in rules_dict.items():
#     print(key, value)

    # print(type(key))


def contains(bag_rule, my_bag):
    sum = 0
    if my_bag in rules_dict.get(bag_rule):
        # print("Found " + my_bag + " in " + bag_rule)
        return 1
    elif "no other" in rules_dict.get(bag_rule):
        # print("Found no other in " + bag_rule)
        return 0
    else:
        # print("Searching " + my_bag + " in " + bag_rule + "...")
        for bag in rules_dict.get(bag_rule):
            sum += contains(bag, my_bag)
        return sum


def count_bags(input_bag):
    count = 0
    for bag_rule in rules_dict:
        if contains(bag_rule, input_bag) > 0:
            # print(bag_rule)
            count += 1
            # print(str(count) + ": " + bag_rule)
    return count


print(count_bags("shiny gold"))
#################### Part One ####################


#################### Part Two ####################
# I was stuck on this part for a long time,
# so I used some help from Bradley Sward's solution:
# https://www.youtube.com/watch?v=4Fr1zSzaUyY

rules_dict_2 = dict()

for rule in rules:
    # print(rule)
    keyBag = rule.split("contain")[0].replace("bags", "").strip()
    # print(keyBag + ":")
    contents_str = rule.split("contain")[1]
    contents_arr = contents_str.split(",")
    for i in range(len(contents_arr)):
        contents_arr[i] = contents_arr[i].rstrip(
            ".").replace("bags", "").replace("bag", "").strip()

    rules_dict_2.update({keyBag: contents_arr})

# for key, value in rules_dict_2.items():
#     print(key, value)

total = -1

bags = {"shiny gold": 1}

while len(bags) > 0:
    # print(bags)
    # print()
    key = list(bags.keys())[0]
    total += bags[key]
    if key in rules_dict_2 and "no other" not in rules_dict_2[key]:
        for newbag in rules_dict_2[key]:
            newbag_name = newbag.split(" ")[1]+" "+newbag.split(" ")[2]
            if newbag_name not in bags:
                bags[newbag_name] = 0
            bags[newbag_name] += (list(bags.values())[0] * int(newbag[0]))
    del bags[key]

print(total)
#################### Part Two ####################
