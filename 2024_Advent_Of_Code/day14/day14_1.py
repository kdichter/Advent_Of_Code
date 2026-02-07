import re

grid_rows = 103
grid_cols = 101
seconds = 100

grid = [[0] * grid_cols for _ in range(grid_rows)]

rows = len(grid)
cols = len(grid[0])
for line in open("day14_data.txt").read().split('\n'):
    col, row, v_col, v_row = map(int, re.findall(r'-?\d+', line))

    new_row = (row + v_row * seconds) % rows
    new_col = (col + v_col * seconds) % cols

    grid[new_row][new_col] += 1

q1, q2, q3, q4 = 0, 0, 0, 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] != 0:
            if i < rows // 2 and j < cols // 2:
                q2 += grid[i][j]
            elif i < rows // 2 and j > cols // 2:
                q1 += grid[i][j]
            elif i > rows // 2 and j < cols // 2:
                q3 += grid[i][j]
            elif i > rows // 2 and j > cols // 2:
                q4 += grid[i][j]

# for row in grid:
#     print(''.join(str(x) for x in row))

total = q1 * q2 * q3 * q4
print(total)
