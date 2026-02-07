with open("day10_data.txt", "r") as file:
    data = [[int(x) for x in line.strip()] for line in file]


def score(row, col):
    if data[row][col] == 9:
        return {(row, col)}

    result = set()
    curr = data[row][col]

    for dir_row, dir_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dir_row, col + dir_col
        if 0 <= new_row < len(data) and 0 <= new_col < len(data[row]):
            if data[new_row][new_col] == curr + 1:
                result |= score(new_row, new_col)

    return result


total = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            s = len(score(i, j))
            total += s
print(total)
