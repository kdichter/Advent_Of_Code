with open("day12_data.txt", "r") as file:
    plots = [[x for x in line.strip()] for line in file]


def explore(data, visited, symbol, row, col):
    visited.add((row, col))
    area = 1
    perimeter = 0

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc

        if (0 <= nr < len(data) and
                0 <= nc < len(data[nr]) and
                data[nr][nc] == symbol
        ):
            if (nr, nc) not in visited:
                a, p = explore(data, visited, symbol, nr, nc)
                area += a
                perimeter += p
        else:
            perimeter += 1

    return area, perimeter


visited = set()
total = 0
for i in range(len(plots)):
    for j in range(len(plots[i])):
        if (i, j) not in visited:
            symbol = plots[i][j]
            area, perimeter = explore(plots, visited, symbol, i, j)
            total += area * perimeter
print(total)
