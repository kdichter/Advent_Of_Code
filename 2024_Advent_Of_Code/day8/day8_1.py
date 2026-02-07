from collections import defaultdict

antennas = defaultdict(list)
with open("day8_data.txt", "r") as lines:
    data = [line.strip() for line in lines]

for row in range(len(data)):
    for col in range(len(data[row])):
        val = data[row][col]
        if val == '.':
            continue
        antennas[val].append((row, col))

total = set()
for antenna in antennas:
    for i in range(len(antennas[antenna])):
        for j in range(i + 1, len(antennas[antenna])):
            x_dist = antennas[antenna][j][0] - antennas[antenna][i][0]
            y_dist = antennas[antenna][j][1] - antennas[antenna][i][1]

            a1_x = antennas[antenna][i][0] - x_dist
            a1_y = antennas[antenna][i][1] - y_dist
            a2_x = antennas[antenna][j][0] + x_dist
            a2_y = antennas[antenna][j][1] + y_dist

            if 0 <= a1_x < len(data) and 0 <= a1_y < len(data[0]):
                # print(f'({a1_x}, {a1_y})')
                total.add((a1_x, a1_y))
            if 0 <= a2_x < len(data) and 0 <= a2_y < len(data[0]):
                # print(f'({a2_x}, {a2_y})')
                total.add((a2_x, a2_y))

print(len(total))
# print(antennas)
