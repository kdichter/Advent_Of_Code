from collections import defaultdict

antennas = defaultdict(list)
with open("day8_test.txt", "r") as lines:
    data = [[x for x in line.strip()] for line in lines]

for row in range(len(data)):
    for col in range(len(data[row])):
        val = data[row][col]
        if val == '.':
            continue
        antennas[val].append((row, col))

total = set()
for antenna in antennas:
    positions = antennas[antenna]
    for i in range(len(antennas[antenna])):
        total.add(positions[i])
        for j in range(i + 1, len(antennas[antenna])):
            total.add(positions[j])
            x_dist = antennas[antenna][j][0] - antennas[antenna][i][0]
            y_dist = antennas[antenna][j][1] - antennas[antenna][i][1]

            a1_x = antennas[antenna][i][0] - x_dist
            a1_y = antennas[antenna][i][1] - y_dist
            a2_x = antennas[antenna][j][0] + x_dist
            a2_y = antennas[antenna][j][1] + y_dist

            while 0 <= a1_x < len(data) and 0 <= a1_y < len(data[0]):
                total.add((a1_x, a1_y))
                if data[a1_x][a1_y] == '.':
                    data[a1_x][a1_y] = '#'
                a1_x = a1_x - x_dist
                a1_y = a1_y - y_dist

            while 0 <= a2_x < len(data) and 0 <= a2_y < len(data[0]):
                total.add((a2_x, a2_y))
                if data[a2_x][a2_y] == '.':
                    data[a2_x][a2_y] = '#'
                a2_x = a2_x + x_dist
                a2_y = a2_y + y_dist

for line in data:
    print(''.join(line))
print(len(total))
# print(antennas)
