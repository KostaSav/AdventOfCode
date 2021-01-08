import copy

seats = []

with open('2020\day11.txt', 'r') as f:
    for line in f.readlines():
        seats.append(list(line.strip('\n')))

# Print the seating layout to the console


def print_layout(layout):
    print('__________________________________________________')
    for row in layout:
        print(row)
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print()

#################### Part One ####################

# Check the 8 adjacent spots around the seat in coordinates row and col,
# return False if even one of them is occupied


def without_adjacents(layout, row, col):
    if (row > 0 and col > 0 and layout[row-1][col-1] == "#"):
        return False
    elif (row > 0 and layout[row-1][col] == "#"):
        return False
    elif (row > 0 and col < len(layout[0]) - 1 and layout[row-1][col+1] == "#"):
        return False
    elif (col > 0 and layout[row][col-1] == "#"):
        return False
    elif (col < len(layout[0]) - 1 and layout[row][col+1] == "#"):
        return False
    elif (row < len(layout) - 1 and col > 0 and layout[row+1][col-1] == "#"):
        return False
    elif (row < len(layout) - 1 and layout[row+1][col] == "#"):
        return False
    elif (row < len(layout) - 1 and col < len(layout[0]) - 1 and layout[row+1][col+1] == "#"):
        return False
    else:
        return True

# Count the number of occupied seats adjacent to the seat in row and col,
# return True if they are more than 4


def four_plus_adjacents(layout, row, col):
    count = 0
    if (row > 0 and col > 0 and layout[row-1][col-1] == "#"):
        count += 1
    if (row > 0 and layout[row-1][col] == "#"):
        count += 1
    if (row > 0 and col < len(layout[0]) - 1 and layout[row-1][col+1] == "#"):
        count += 1
    if (col > 0 and layout[row][col-1] == "#"):
        count += 1
    if (col < len(layout[0]) - 1 and layout[row][col+1] == "#"):
        count += 1
    if (row < len(layout) - 1 and col > 0 and layout[row+1][col-1] == "#"):
        count += 1
    if (row < len(layout) - 1 and layout[row+1][col] == "#"):
        count += 1
    if (row < len(layout) - 1 and col < len(layout[0]) - 1 and layout[row+1][col+1] == "#"):
        count += 1
    if count >= 4:
        return True
    else:
        return False

# Based on the current seating layout, occupy or free seats
# and return the new seating layout


def occupy_seats(layout):
    output = copy.deepcopy(layout)

    for row in range(len(layout)):
        for col in range(len(layout[0])):
            if layout[row][col] == 'L' and without_adjacents(layout, row, col):
                output[row][col] = '#'
            elif layout[row][col] == '#' and four_plus_adjacents(layout, row, col):
                output[row][col] = 'L'
    # print_layout(output)
    return output


# print_layout(seats)

# Start the process of occupying or freeing seats,
# until the number of occupied seats remains stable

# previous_layout = seats
# next_layout = occupy_seats(seats)

# print_layout(previous_layout)
# print_layout(next_layout)

# while sum(x.count("#") for x in previous_layout) != sum(x.count("#") for x in next_layout):
#     previous_layout = next_layout
#     next_layout = occupy_seats(next_layout)
#     # print_layout(next_layout)
# print(sum(x.count("#") for x in next_layout))
#################### Part One ####################


#################### Part Two ####################

# Check the 8 directions around the seat in coordinates row and col,
# return False if even one of them is occupied
def without_adjacents_2(layout, row, col):
    return check_up_left(layout, row, col) and check_up(layout, row, col) and check_up_right(layout, row, col) and check_right(layout, row, col) and check_down_right(layout, row, col) and check_down(layout, row, col) and check_down_left(layout, row, col) and check_left(layout, row, col)

# Count the number of occupied seats in the 8 directions around the seat in row and col,
# return True if they are more than 5


def five_plus_visible(layout, row, col):
    count = 0
    if not check_up_left(layout, row, col):
        count += 1
    if not check_up(layout, row, col):
        count += 1
    if not check_up_right(layout, row, col):
        count += 1
    if not check_right(layout, row, col):
        count += 1
    if not check_down_right(layout, row, col):
        count += 1
    if not check_down(layout, row, col):
        count += 1
    if not check_down_left(layout, row, col):
        count += 1
    if not check_left(layout, row, col):
        count += 1
    if count >= 5:
        return True
    else:
        return False

# Eight functions checking each direction around a seat,
# returns False if that direction finds an occupied seat first,
# True if it does not or if it finds an empty one


def check_up_left(layout, row, col):
    while (row > 0 and col > 0):
        if layout[row-1][col-1] == "#":
            return False
        elif layout[row-1][col-1] == "L":
            return True
        else:
            row -= 1
            col -= 1
    return True


def check_up(layout, row, col):
    while (row > 0):
        if layout[row-1][col] == "#":
            return False
        elif layout[row-1][col] == "L":
            return True
        else:
            row -= 1
    return True


def check_up_right(layout, row, col):
    while (row > 0 and col < len(layout[0]) - 1):
        if layout[row-1][col+1] == "#":
            return False
        elif layout[row-1][col+1] == "L":
            return True
        else:
            row -= 1
            col += 1
    return True


def check_right(layout, row, col):
    while (col < len(layout[0]) - 1):
        if layout[row][col+1] == "#":
            return False
        elif layout[row][col+1] == "L":
            return True
        else:
            col += 1
    return True


def check_right(layout, row, col):
    while (col < len(layout[0]) - 1):
        if layout[row][col+1] == "#":
            return False
        elif layout[row][col+1] == "L":
            return True
        else:
            col += 1
    return True


def check_down_right(layout, row, col):
    while (row < len(layout) - 1 and col < len(layout[0]) - 1):
        if layout[row+1][col+1] == "#":
            return False
        elif layout[row+1][col+1] == "L":
            return True
        else:
            row += 1
            col += 1
    return True


def check_down(layout, row, col):
    while (row < len(layout) - 1):
        if layout[row+1][col] == "#":
            return False
        elif layout[row+1][col] == "L":
            return True
        else:
            row += 1
    return True


def check_down_left(layout, row, col):
    while (row < len(layout) - 1 and col > 0):
        if layout[row+1][col-1] == "#":
            return False
        elif layout[row+1][col-1] == "L":
            return True
        else:
            row += 1
            col -= 1
    return True


def check_left(layout, row, col):
    while (col > 0):
        if layout[row][col-1] == "#":
            return False
        elif layout[row][col-1] == "L":
            return True
        else:
            col -= 1
    return True


# Based on the current seating layout, occupy or free seats using the new rules
# and return the new seating layout
def occupy_seats_2(layout):
    output = copy.deepcopy(layout)

    for row in range(len(layout)):
        for col in range(len(layout[0])):
            if layout[row][col] == 'L' and without_adjacents_2(layout, row, col):
                output[row][col] = '#'
            elif layout[row][col] == '#' and five_plus_visible(layout, row, col):
                output[row][col] = 'L'
    # print_layout(output)
    return output


# print_layout(seats)

# Start the process of occupying or freeing seats,
# until the number of occupied seats remains stable

previous_layout = seats
next_layout = occupy_seats_2(seats)
# print_layout(previous_layout)
# print_layout(next_layout)

while sum(x.count("#") for x in previous_layout) != sum(x.count("#") for x in next_layout):
    previous_layout = next_layout
    next_layout = occupy_seats_2(next_layout)
    # print_layout(next_layout)
print(sum(x.count("#") for x in next_layout))

#################### Part Two ####################
