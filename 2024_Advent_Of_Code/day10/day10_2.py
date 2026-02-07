with open("day10_data.txt", "r") as file:
    data = [[int(x) for x in line.strip()] for line in file]

dirs = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}


def score(row, col, curr_num, direction):
    if curr_num == 9:
        return 1
    up = score(row - 1, col, curr_num + 1, dirs[1]) if direction != dirs[0] and row - 1 >= 0 and \
                                                       data[row - 1][col] == curr_num + 1 else 0
    down = score(row + 1, col, curr_num + 1, dirs[0]) if direction != dirs[1] and row + 1 < len(data) and \
                                                         data[row + 1][col] == curr_num + 1 else 0
    left = score(row, col - 1, curr_num + 1, dirs[3]) if direction != dirs[2] and col - 1 >= 0 and \
                                                         data[row][col - 1] == curr_num + 1 else 0
    right = score(row, col + 1, curr_num + 1, dirs[2]) if direction != dirs[3] and col + 1 < len(
        data[row]) and data[row][col + 1] == curr_num + 1 else 0

    return up + down + left + right


total = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            s = score(i, j, 0, None)
            total += s
print(total)
