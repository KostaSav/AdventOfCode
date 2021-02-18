with open("2020\day15.txt", "r") as f:
    numbers = f.read().replace("\n", "")

#################### Part One ####################
# Convert our input to an array of integers
starting = [int(x) for x in numbers.split(",")]
count = len(starting)

while count < 2020:
    last_number = starting[count - 1]
    # Exclude the last number from our search
    previous_array = starting[: count - 1]

    # Find the previous occurence of our last array number, else append 0
    if last_number in previous_array:
        pos = len(previous_array) - 1 - previous_array[::-1].index(last_number)
        starting.append(count - 1 - pos)
    else:
        starting.append(0)

    count += 1


print(starting[2019])
#################### Part One ####################


#################### Part Two ####################
# Probably not the best solution, given the time it takes to complete...
# Used a dictionary to store each value as a key only once and their last position as a value
positions = dict()

initial = [int(x) for x in numbers.split(",")]
last_number = initial[len(initial) - 1]
count = 1

for number in initial[:-1]:
    positions.update({number: count})
    count += 1


while count <= 30000000:
    if last_number in positions.keys():
        temp = last_number
        last_number = count - positions[last_number]
        positions.update({temp: count})
        if count == 30000000:
            print(temp)
        count += 1
    else:
        positions.update({last_number: count})
        if count == 30000000:
            print(temp)
        count += 1
        last_number = 0
#################### Part Two ####################