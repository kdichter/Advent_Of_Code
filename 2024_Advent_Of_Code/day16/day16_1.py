import heapq

grid = [list(line.strip()) for line in open("day16_data.txt", "r")]

s_row, s_col = len(grid) - 2, 1
e_row, e_col = 1, len(grid[0]) - 2
dirs = [(0, -1, 'W'), (0, 1, 'E'), (-1, 0, 'S'), (1, 0, 'N')]


def manhattan_distance(row, col):
    return abs(e_row - row) + abs(e_col - col)


def shortest_path():
    # f, g, direction, row, col
    pq = []
    heapq.heappush(pq, (manhattan_distance(s_row, s_col), 0, 'E', s_row, s_col))

    g_cost = {(s_row, s_col): 0}
    came_from = {}

    while pq:
        f, g, d, row, col = heapq.heappop(pq)

        if (row, col) == (e_row, e_col):
            # reconstruct path
            cur = (row, col)
            while cur != (s_row, s_col):
                r, c = cur
                grid[r][c] = 'O'
                cur = came_from[cur]
            return g

        for dr, dc, nd in dirs:
            nr, nc = row + dr, col + dc

            if grid[nr][nc] == '#':
                continue

            new_g = g + 1

            if (nr, nc) not in g_cost or new_g < g_cost[(nr, nc)]:
                if nd != d:
                    new_g += 1000
                g_cost[(nr, nc)] = new_g
                came_from[(nr, nc)] = (row, col)
                h = manhattan_distance(nr, nc)
                heapq.heappush(pq, (new_g + h, new_g, nd, nr, nc))

    return None


result = shortest_path()

for line in grid:
    print(''.join(line))

print(result)
