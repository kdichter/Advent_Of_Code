file = open("day7_test.txt", "r")

grid = []

for line in file:
    grid.append([x for x in line.strip()])

row_start = 0
col_start = grid[row_start].index('S')
cache = {}


def backtrack(grid, row, col):
    next_row = row + 1
    next_col = col

    if next_row >= len(grid):
        return 1

    if next_col < 0 or next_col >= len(grid[0]):
        return 0

    if (next_row, next_col) in cache:
        return cache[(next_row, next_col)]

    if grid[next_row][next_col] == '.':
        cache[(next_row, next_col)] = backtrack(grid, next_row, next_col)
        return cache[(next_row, next_col)]
    else:
        cache[(next_row, next_col - 1)] = backtrack(grid, next_row, next_col - 1)
        cache[(next_row, next_col + 1)] = backtrack(grid, next_row, next_col + 1)
        return cache[(next_row, next_col - 1)] + cache[(next_row, next_col + 1)]


total = backtrack(grid, row_start, col_start)
for line in grid:
    print(line)
print(total)
