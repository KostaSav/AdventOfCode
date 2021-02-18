with open("2020\day15.txt", "r") as f:
    starting = f.read().replace("\n", "")

#################### Part One ####################
# Convert our input to an array of integers
starting = [int(x) for x in starting.split(",")]
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