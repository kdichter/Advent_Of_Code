with open("day15_data.txt", "r") as file:
    old_grid, moves = file.read().strip().split('\n\n')

row, col = 0, 0
old_grid = [list(line) for line in old_grid.splitlines()]

grid = []
for line in old_grid:
    string = ''
    for char in line:
        if char == '#':
            string += '##'
        elif char == '.':
            string += '..'
        elif char == 'O':
            string += '[]'
        else:
            string += '@.'
    grid.append(list(string))

for row, x in enumerate(grid):
    if '@' in x:
        col = x.index('@')
        break

moves = moves.replace('\n', '')
dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}


def create_segment(visited, queue, row, col):
    segment = []

    while grid[row][col] != '.':
        visited.add((row, col))
        if grid[row][col] == '[':
            if (row, col + 1) not in visited:
                queue.append((row, col + 1))
        elif grid[row][col] == ']':
            if (row, col - 1) not in visited:
                queue.append((row, col - 1))
        else:
            return ['#']
        segment.append(grid[row][col])
        row += dirs[move][0]

    return segment


for move in moves:
    dy, dx = dirs[move]
    new_row, new_col = row + dy, col + dx

    if grid[new_row][new_col] == '#':
        continue

    elif grid[new_row][new_col] == '.':
        grid[row][col] = '.'
        grid[new_row][new_col] = '@'
        row, col = new_row, new_col

    elif grid[new_row][new_col] in ('[', ']'):
        r, c = new_row, new_col

        if move == '<' or move == '>':
            while grid[r][c] in ('[', ']'):
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
            valid = True
            rr, cc = r, c
            queue = [(rr, cc)]
            visited = {(row, col), (rr, cc)}
            segments = []

            while len(queue) > 0:
                rrr, ccc = queue.pop(0)
                new_segment = create_segment(visited, queue, rrr, ccc)
                if '#' in new_segment:
                    valid = False
                    break
                segments.append((rrr, ccc, new_segment))

            if valid:
                for row, col in visited:
                    grid[row][col] = '.'

                for row_idx, col_idx, segment in segments:
                    if move == '^':
                        for i, val in enumerate(segment):
                            grid[row_idx - 1 - i][col_idx] = val
                    else:
                        for i, val in enumerate(segment):
                            grid[row_idx + 1 + i][col_idx] = val

                grid[new_row][new_col] = '@'

                row, col = new_row, new_col
total = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == '[':
            total += 100 * row + col

for line in grid:
    print(''.join(line))

print(total)
