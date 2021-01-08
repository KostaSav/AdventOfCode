with open('2020\day3.txt', 'r') as f:
    area = [line.strip() for line in f]


def traverse(right, down):
    x = 0
    y = 0
    trees = 0
    currentPosition = area[x][y]

    while x < len(area)-1:
        x += down

        if(y < len(area[0])-right):
            y += right
        else:
            y = right - (len(area[0]) - y)

        currentPosition = area[x][y]
        if currentPosition == "#":
            trees += 1

    return(trees)


#################### Part 1 ####################
print(traverse(3, 1))
#################### Part 1 ####################


#################### Part 2 ####################
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
product = 1
for i in range(len(slopes)):
    product *= traverse(slopes[i][0], slopes[i][1])
print(product)
#################### Part 2 ####################
