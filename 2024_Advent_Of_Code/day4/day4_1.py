with open("day4_data.txt", "r") as lines:
    data = [[x for x in line.strip()] for line in lines]


def search_horizontal(row, col):
    total = 0
    # left
    if col - 3 > -1 and ''.join(data[row][col - 3:col + 1]) == 'SAMX':
        total += 1
    # right
    if col + 3 <= len(data[row]) - 1 and ''.join(data[row][col:col + 4]) == 'XMAS':
        total += 1
    return total


def search_vertical(row, col):
    total = 0
    # up
    if row - 3 > -1 and ''.join(r[col] for r in data[row - 3: row + 1]) == 'SAMX':
        total += 1
    # down
    if row + 3 <= len(data[row]) - 1 and ''.join(r[col] for r in data[row:row + 4]) == 'XMAS':
        total += 1
    return total


def search_diagonal_top_down(row, col):
    total = 0
    n_rows = len(data)
    n_cols = len(data[row])
    # down right
    if col + 3 < n_cols and row + 3 < n_rows:
        seq = ''.join(data[row + i][col + i] for i in range(4))
        if seq == 'XMAS':
            total += 1
    # down left
    if col - 3 > -1 and row + 3 < n_rows:
        seq = ''.join(data[row + i][col - i] for i in range(4))
        if seq == 'XMAS':
            total += 1
    return total


def search_diagonal_bottom_up(row, col):
    total = 0
    n_cols = len(data[row])
    # up right
    if col + 3 < n_cols and row - 3 > -1:
        seq = ''.join(data[row - i][col + i] for i in range(4))
        if seq == 'XMAS':
            total += 1
    # up left
    if col - 3 > -1 and row - 3 > -1:
        seq = ''.join(data[row - i][col - i] for i in range(4))
        if seq == 'XMAS':
            total += 1
    return total


total = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'X':
            total += search_horizontal(i, j)
            total += search_vertical(i, j)
            total += search_diagonal_top_down(i, j)
            total += search_diagonal_bottom_up(i, j)
print(total)
