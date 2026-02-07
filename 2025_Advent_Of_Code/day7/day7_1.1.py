file = open("day7_test.txt", "r")

grid = []

for line in file:
    grid.append([x for x in line.strip()])

row_start = 0
col_start = grid[row_start].index('S')
queue = [(row_start, col_start)]

visited = {(row_start, col_start)}
total = 0
while len(queue) > 0:
    row, col = queue.pop(0)

    next_row = row + 1
    next_col = col

    if next_row >= len(grid):
        continue

    if next_col < 0 or next_col >= len(grid[0]):
        continue

    if (next_row, next_col) in visited:
        continue

    grid[row][col] = '|'
    if grid[next_row][next_col] == '.':
        queue.append((next_row, next_col))
        visited.add((next_row, next_col))
    else:
        total += 1
        queue.append((next_row, next_col - 1))
        queue.append((next_row, next_col + 1))
        visited.add((next_row, next_col - 1))
        visited.add((next_row, next_col + 1))

for line in grid:
    print(line)
print(total)
