with open('2020\day12.txt', 'r') as f:
    instructions = [line.strip() for line in f]

# print(instructions)

#################### Part One ####################

# horizon_distances = {
#     "N": 0,
#     "E": 0,
#     "S": 0,
#     "W": 0
# }

# horizon_positions = ["N", "E", "S", "W"]

# current_position = "E"

# for action in instructions:
#     direction = action[0]
#     value = int(action[1:])

#     if direction == "N" or direction == "S" or direction == "E" or direction == "W":
#         horizon_distances[direction] += value
#     elif direction == "F":
#         horizon_distances[current_position] += value
#     else:
#         current_index = horizon_positions.index(current_position)
#         steps = value // 90
#         steps = steps % 4

#         if direction == "R":
#             for i in range(steps):
#                 if current_index == len(horizon_positions)-1:
#                     current_index = 0
#                 else:
#                     current_index += 1
#         else:
#             for i in range(steps):
#                 if current_index == 0:
#                     current_index = len(horizon_positions)-1
#                 else:
#                     current_index -= 1

#         current_position = horizon_positions[current_index]

# Manhattan_distance = abs(horizon_distances["N"]-horizon_distances["S"]) + abs(
#     horizon_distances["E"]-horizon_distances["W"])

# print(Manhattan_distance)

#################### Part One ####################


#################### Part TWo ####################
## Used some much needed help from
## https://github.com/TheMorpheus407/AdventOfCode2020/blob/master/12.py

waypoint = {
    "N": 1,
    "E": 10,
    "S": 0,
    "W": 0
}

pos = [0, 0]

horizon_positions = ["N", "E", "S", "W"]

for action in instructions:
    direction = action[0]
    value = int(action[1:])

    if direction == "N" or direction == "S" or direction == "E" or direction == "W":
        waypoint[direction] += value
    elif direction == "F":
        pos[0] += value * (waypoint["E"]-waypoint["W"])
        pos[1] += value * (waypoint["N"]-waypoint["S"])

    else:
        value = value // 90

        if direction == "R":
            for i in range(value):
                last_waypoint = waypoint[horizon_positions[len(
                    horizon_positions)-1]]
                for j in range(len(horizon_positions)):
                    temp = waypoint[horizon_positions[j]]
                    waypoint[horizon_positions[j]] = last_waypoint
                    last_waypoint = temp
        else:
            for i in range(value):
                first_waypoint = waypoint[horizon_positions[0]]
                for j in range(len(horizon_positions)-1, -1, -1):
                    temp = waypoint[horizon_positions[j]]
                    waypoint[horizon_positions[j]] = first_waypoint
                    first_waypoint = temp


Manhattan_distance = abs(pos[0]) + abs(pos[1])

print(Manhattan_distance)

#################### Part TWo ####################
