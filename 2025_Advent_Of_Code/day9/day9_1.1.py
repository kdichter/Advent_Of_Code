with open("day9_test.txt", "r") as file:
    points = [[int(x) for x in line.strip().split(',')] for line in file]
# points.sort(key=lambda x: int(x[0]))
l1 = sorted(points, key=lambda p: (p[0], p[1]))
l2 = sorted(points, key=lambda p: (p[0], -p[1]))

max_area = 0
last_points = [l1[0], l1[len(l1) - 1], l2[len(l2) - 1], l2[0]]
for i in range(len(last_points)):
    for j in range(len(last_points)):
        max_area = max(max_area,
                       (abs(last_points[i][0] - last_points[j][0]) + 1) * (
                               abs(last_points[i][1] - last_points[j][1]) + 1))

print(last_points)
print(max_area)
