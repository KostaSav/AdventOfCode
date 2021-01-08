with open('day1.txt', 'r') as f:
    entries_str = [line.strip() for line in f]

expenses = []
for entry in entries_str:
    expenses.append(int(entry))

expenses.sort()
# print(expenses)


# Part 1
first = 0
second = 0
found = False

for i in range(0, len(expenses), 1):
    for j in range(len(expenses)-1, -1, -1):
        if expenses[i]+expenses[j] == 2020:
            found = True
            first = i
            second = j
            break
        elif expenses[i]+expenses[j] < 2020:
            break
        else:
            continue

    if found:
        break

# Part 2
first = 0
second = 0
third = 0
found = False

for i in range(0, len(expenses)-1):
    for j in range(i+1, len(expenses)):
        sum = expenses[i] + expenses[j]
        rem = 2020 - sum
        if sum > 2020:
            break
        elif rem in expenses:
            found = True
            first = i
            second = j
            third = expenses.index(rem)
            break

    if found:
        break


print("first = " + str(first) + ", second = " +
      str(second) + ", third = " + str(third))
print("expenses[first] = " + str(expenses[first]) +
      ", expenses[second] = " + str(expenses[second]) +
      ", expenses[third] = " + str(expenses[third]))
print("expenses[first]+expenses[second]+expenses[third] = " +
      str(expenses[first]+expenses[second]+expenses[third]))
print("expenses[first]*expenses[second]*expenses[third] = " +
      str(expenses[first]*expenses[second]*expenses[third]))
