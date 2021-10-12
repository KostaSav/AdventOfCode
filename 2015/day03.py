with open("2015\day03.txt", "r") as f:
    moves_str = f.read()

# ------ Part One ------ #

# Create a set (houses) containing tuples (coordinates)
x = y = 0
visited = set()
visited.add((x, y))

# Move according to the directions
# and add the new coordinates to the visited houses
for move in moves_str:
    if move == "^":
        y -= 1
    elif move == "v":
        y += 1
    elif move == ">":
        x += 1
    else:
        x -= 1
    visited.add((x, y))

print(len(visited))

# ------ End of Part One ------ #


# ------ Part Two ------ #

# Create two set (houses) containing tuples (coordinates),
# one for the santa and one for the robot
santa_x = santa_y = 0
robot_x = robot_y = 0
visited_2 = set()
visited_2.add((santa_x, santa_y))
visited_2.add((robot_x, robot_y))
print(visited_2)

# Move the santa and the robot independently
for i in range(len(moves_str)):
    if (i % 2) == 0:
        if moves_str[i] == "^":
            santa_y -= 1
        elif moves_str[i] == "v":
            santa_y += 1
        elif moves_str[i] == ">":
            santa_x += 1
        else:
            santa_x -= 1
        visited_2.add((santa_x, santa_y))
    else:
        if moves_str[i] == "^":
            robot_y -= 1
        elif moves_str[i] == "v":
            robot_y += 1
        elif moves_str[i] == ">":
            robot_x += 1
        else:
            robot_x -= 1
        visited_2.add((robot_x, robot_y))

print(len(visited_2))

# ------ End of Part Two ------ #