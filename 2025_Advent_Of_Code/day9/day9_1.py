with open("day9_data.txt", "r") as file:
    points = [[int(x) for x in line.strip().split(',')] for line in file]

max_area = 0
for i in range(len(points)):
    for j in range(len(points)):
        max_area = max(max_area,
                       (abs(points[i][0] - points[j][0]) + 1) * (
                               abs(points[i][1] - points[j][1]) + 1))

print(points)
print(max_area)
