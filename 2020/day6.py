with open('2020\day6.txt', 'r') as f:
    answers = [line.strip() for line in f]

# print(answers)
yes = set(())
sum = 0

for line in answers:
    if len(line) > 0:
        for char in line:
            yes.add(char)
    else:
        sum += len(yes)
        yes.clear()
sum += len(yes)

print(sum)
