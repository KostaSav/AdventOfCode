with open('2020\day12.txt', 'r') as f:
    instructions = [line.strip() for line in f]

# print(instructions)

#################### Part One ####################

horizon_distances = {
    "N": 0,
    "E": 0,
    "S": 0,
    "W": 0
}

horizon_positions = ["N", "E", "S", "W"]

current_position = "E"

for action in instructions:
    direction = action[0]
    value = int(action[1:])

    if direction == "N" or direction == "S" or direction == "E" or direction == "W":
        horizon_distances[direction] += value
    elif direction == "F":
        horizon_distances[current_position] += value
    else:
        current_index = horizon_positions.index(current_position)
        steps = value // 90
        steps = steps % 4

        if direction == "R":
            for i in range(steps):
                if current_index == len(horizon_positions)-1:
                    current_index = 0
                else:
                    current_index += 1
        else:
            for i in range(steps):
                if current_index == 0:
                    current_index = len(horizon_positions)-1
                else:
                    current_index -= 1

        current_position = horizon_positions[current_index]

Manhattan_distance = abs(horizon_distances["N"]-horizon_distances["S"]) + abs(
    horizon_distances["E"]-horizon_distances["W"])

print(Manhattan_distance)

#################### Part One ####################
