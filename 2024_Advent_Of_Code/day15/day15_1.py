with open("day15_data.txt", "r") as file:
    grid, moves = file.read().strip().split('\n\n')

row, col = 0, 0
grid = [list(line) for line in grid.splitlines()]
for row, x in enumerate(grid):
    if '@' in x:
        col = x.index('@')
        break

moves = moves.replace('\n', '')
dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
for move in moves:
    dy, dx = dirs[move]
    new_row, new_col = row + dy, col + dx

    if grid[new_row][new_col] == '#':
        continue

    elif grid[new_row][new_col] == '.':
        grid[row][col] = '.'
        grid[new_row][new_col] = '@'
        row, col = new_row, new_col

    elif grid[new_row][new_col] == 'O':
        r, c = new_row, new_col

        if move == '<' or move == '>':
            while grid[r][c] == 'O':
                c += dirs[move][1]
            if grid[r][c] != '#':
                left = min(col, c)
                right = max(col, c)

                segment = grid[row][left:right + 1]

                if move == '<':
                    segment = segment[1:] + ['.']
                else:
                    segment = ['.'] + segment[:-1]

                grid[row][left:right + 1] = segment
                grid[row][col] = '.'
                grid[new_row][new_col] = '@'
                row, col = new_row, new_col

        if move == '^' or move == 'v':
            while grid[r][c] == 'O':
                r += dirs[move][0]
            if grid[r][c] != '#':
                top = min(row, r)
                bottom = max(row, r)

                segment = [grid[i][col] for i in range(top, bottom + 1)]

                if move == '^':
                    segment = segment[1:] + ['.']
                else:
                    segment = ['.'] + segment[:-1]

                for i, val in enumerate(segment, start=top):
                    grid[i][col] = val
                grid[row][col] = '.'
                grid[new_row][new_col] = '@'
                row, col = new_row, new_col

total = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == 'O':
            total += 100 * row + col

print(total)

# for line in grid:
#     print(''.join(line))
# print(moves)
