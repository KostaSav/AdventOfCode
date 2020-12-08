with open('2020\day7.txt', 'r') as f:
    rules = [line.strip() for line in f]

# print(rules)

container = []
contents = []
rules_dict = dict()

for rule in rules:
    # print(rule)
    # container.append(rule.split("contain")[0])
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

