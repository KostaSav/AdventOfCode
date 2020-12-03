import math

with open('2019/day1.txt', 'r') as f:
    entries_str = [line.strip() for line in f]

sum_part_1 = 0
sum_part_2 = 0


def recursive_fuel(mass):
    total = 0
    module = math.floor(mass/3) - 2
    while module > 0:
        total += module
        module = math.floor(module/3) - 2
    return total


for x in entries_str:
    sum_part_1 += math.floor(int(x)/3) - 2
    sum_part_2 += recursive_fuel(int(x))

print(sum_part_1)
print(sum_part_2)
