data = []
line_num = 0

with open("day6_data.txt", "r") as lines:
    for line in lines:
        data.append([x for x in line.strip()])
        idx = line.find('^')
        if idx > -1:
            rr = line_num
            cc = idx
        line_num += 1

dirs = {0: 'up', 1: 'right', 2: 'down', 3: 'left'}


def is_loop(data):
    row, col = rr, cc
    i = 0
    dir = dirs[i]
    visited = set()

    while True:
        visited.add((row, col, dir))

        if dir == 'up':
            next_pos = row - 1, col
        elif dir == 'down':
            next_pos = row + 1, col
        elif dir == 'left':
            next_pos = row, col - 1
        else:
            next_pos = row, col + 1

        if not (-1 < next_pos[0] < len(data) and -1 < next_pos[1] < len(data[0])):
            return False

        if data[next_pos[0]][next_pos[1]] == '#':
            i += 1
            dir = dirs[(i) % len(dirs)]

        else:
            row = next_pos[0]
            col = next_pos[1]

        if (next_pos[0], next_pos[1], dir) in visited:
            return True


total = 0
for r in range(len(data)):
    for c in range(len(data[r])):
        if data[r][c] != '.':
            continue
        data[r][c] = '#'
        if is_loop(data):
            total += 1
        data[r][c] = '.'

print(total)
