import string

with open('2020\day6.txt', 'r') as f:
    answers = [line.strip() for line in f]


########## Part One ##########
yes = set(())
sum_part_1 = 0

for line in answers:
    if len(line) > 0:
        for char in line:
            yes.add(char)
    else:
        sum_part_1 += len(yes)
        yes.clear()
sum_part_1 += len(yes)
yes.clear()

print(sum_part_1)


########## Part Two ##########
alphabet = dict.fromkeys(string.ascii_lowercase, 0)
sum_part_2 = 0
count = 0

for line in answers:
    if len(line) > 0:
        count += 1
        for char in line:
            alphabet[char] =  alphabet.get(char, 0) + 1
    else:
        print(alphabet)
        print(count)
        print()
        for q in alphabet:
            if(alphabet[q] == count):
                sum_part_2 += 1
        count = 0
        alphabet.clear()

for q in alphabet:
    if(alphabet[q] == count):
        sum_part_2 += 1

print(sum_part_2)