file = open("day7_test.txt", "r")

data = []
total = 0


def get_list(lst):
    output = ""
    for ln in lst:
        output += ''.join(ln) + "\n"
    return output


def add_bars(grid, row, col):
    if col > 0:
        grid[row] = grid[row][:col - 1] + '|' + data[row][col:]
    if col < len(grid[row]) - 1:
        grid[row] = grid[row][:col + 1] + '|' + data[row][col + 2:]


for line in file:
    data.append(line.strip())

s_idx = data[0].index('S')
data[1] = data[1][:s_idx] + '|' + data[1][s_idx + 1:]

for row in range(2, len(data)):
    for col in range(len(data[row])):
        prev_col_val = data[row - 1][col]
        curr_col_val = data[row][col]
        if prev_col_val == '|':
            if curr_col_val == '^':
                add_bars(data, row, col)
                total += 1
            else:
                data[row] = data[row][:col] + '|' + data[row][col + 1:]

print(get_list(data))
print(total)
