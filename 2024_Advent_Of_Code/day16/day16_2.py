import heapq
from collections import defaultdict

grid = [list(line.strip()) for line in open("day16_test.txt", "r")]
parents = defaultdict(list)

s_row, s_col = len(grid) - 2, 1
e_row, e_col = 1, len(grid[0]) - 2
dirs = [(0, -1, 'W'), (0, 1, 'E'), (-1, 0, 'S'), (1, 0, 'N')]


def shortest_path():
    # g, direction, row, col
    end_cost = 0
    pq = []
    heapq.heappush(pq, (0, 'E', s_row, s_col))

    g_cost = {(s_row, s_col): 0}

    while pq:
        g, d, row, col = heapq.heappop(pq)

        if g > g_cost[(row, col)]:
            continue

        if (row, col) == (e_row, e_col):
            end_cost = g
            break

        for dr, dc, nd in dirs:
            nr, nc = row + dr, col + dc

            if grid[nr][nc] == '#':
                continue

            new_g = g + 1

            if (nr, nc) not in g_cost or new_g < g_cost[(nr, nc)]:
                if nd != d:
                    new_g += 1000
                g_cost[(nr, nc)] = new_g
                parents[(nr, nc)] = [(row, col)]
                heapq.heappush(pq, (new_g, nd, nr, nc))
            elif new_g == g_cost[(nr, nc)]:
                parents[(nr, nc)].append((row, col))

    return end_cost


result = shortest_path()

for line in grid:
    print(''.join(line))

print(result)
