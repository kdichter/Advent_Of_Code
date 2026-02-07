data = []
line_num = 0

with open("day6_test.txt", "r") as lines:
    for line in lines:
        data.append([x for x in line.strip()])
        idx = line.find('^')
        if idx > -1:
            row = line_num
            col = idx
        line_num += 1

visited = set()
idx = 0
dirs = {0: 'up', 1: 'right', 2: 'down', 3: 'left'}
dir = dirs[idx]
while True:
    visited.add((row, col))
    if dir == 'up':
        next_pos = row - 1, col
    elif dir == 'down':
        next_pos = row + 1, col
    elif dir == 'left':
        next_pos = row, col - 1
    else:
        next_pos = row, col + 1

    if not (-1 < next_pos[0] < len(data) and -1 < next_pos[1] < len(data[0])):
        break

    if data[next_pos[0]][next_pos[1]] == '#':
        idx += 1
        dir = dirs[(idx) % len(dirs)]

    else:
        row = next_pos[0]
        col = next_pos[1]

# for line in data:
#     print(''.join(line))
print(len(visited))
