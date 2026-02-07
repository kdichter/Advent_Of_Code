from collections import defaultdict

with open("day12_data.txt", "r") as file:
    plots = [[x for x in line.strip()] for line in file]


def explore(data, visited, symbol, row, col, region):
    visited.add((row, col))
    region.add((row, col))

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc

        if 0 <= nr < len(data) and 0 <= nc < len(data[0]) and data[nr][nc] == symbol:
            if (nr, nc) not in visited:
                explore(data, visited, symbol, nr, nc, region)


def count_sides(region):
    sides = 0

    for r, c in region:
        # True  -> if the cell above is in the region
        # False  -> if it is not
        up = (r - 1, c) in region
        down = (r + 1, c) in region
        left = (r, c - 1) in region
        right = (r, c + 1) in region

        ul = (r - 1, c - 1) in region
        ur = (r - 1, c + 1) in region
        dl = (r + 1, c - 1) in region
        dr = (r + 1, c + 1) in region

        # top-left corner
        if (not up and not left) or (up and left and not ul):
            sides += 1
        # top-right corner
        if (not up and not right) or (up and right and not ur):
            sides += 1
        # bottom-left corner
        if (not down and not left) or (down and left and not dl):
            sides += 1
        # bottom-right corner
        if (not down and not right) or (down and right and not dr):
            sides += 1

    return sides


visited = set()
total = 0

# corners = number of sides
for i in range(len(plots)):
    for j in range(len(plots[0])):
        if (i, j) not in visited:
            region = set()
            explore(plots, visited, plots[i][j], i, j, region)
            area = len(region)
            sides = count_sides(region)
            total += area * sides
print(total)
