import copy

seats = []

with open('2020\day11.txt', 'r') as f:
    for line in f.readlines():
        seats.append(list(line.strip('\n')))


#################### Part One ####################
def print_layout(layout):
    print('__________________________________________________')
    for row in layout:
        print(row)
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print()


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

previous_layout = seats
next_layout = occupy_seats(seats)

# print_layout(previous_layout)
# print_layout(next_layout)

while sum(x.count("#") for x in previous_layout) != sum(x.count("#") for x in next_layout):
    previous_layout = next_layout
    next_layout = occupy_seats(next_layout)
    # print_layout(next_layout)
print(sum(x.count("#") for x in next_layout))
#################### Part One ####################
