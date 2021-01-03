with open('2020\day9.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f]

# print(numbers)

#################### Part One ####################
preamble = 25
index = preamble

while True:
    for i in range(index - preamble, index):
        found = False
        print("i = " + str(i))
        for j in range(i+1, index):
            print("j = " + str(j))
            if numbers[i]+numbers[j] == numbers[index]:
                found = True
                print(str(numbers[i])+" + "+str(numbers[j]) +
                      " = "+str(numbers[index]))
                print()
                break
        if found:
            index += 1
            break
    if not found:
        print("Not found. Index: " + str(index) +
              ", value:" + str(numbers[index]))
        break
#################### Part One ####################


#################### Part Two ####################
total = 0
smallest_index = 0
largest_index = 0

for i in range(index):
    while total > numbers[index]:
        total -= numbers[smallest_index]
        smallest_index += 1

    if total == numbers[index]:
        largest_index = i-1
        print("smallest index: " + str(smallest_index) + " largest index: " +
              str(largest_index))
        break

    total += numbers[i]

contiguous = set()
for k in range(smallest_index, largest_index+1):
    contiguous.add(numbers[k])
print(max(contiguous)+min(contiguous))
#################### Part Two ####################
