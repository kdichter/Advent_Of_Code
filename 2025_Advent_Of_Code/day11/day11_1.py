from collections import deque

server_rack = {}

with open("day11_data.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        key = parts[0][:-1]
        server_rack[key] = parts[1:]

print(server_rack)


def bfs(start):
    queue = deque([start])
    paths = 0

    while len(queue) > 0:
        connection = queue.popleft()

        if connection == 'out':
            paths += 1
            continue

        queue.extend(server_rack[connection])
        # for cable in server_rack[connection]:
        #     queue.append(cable)

    return paths


paths = bfs('you')
print(paths)
