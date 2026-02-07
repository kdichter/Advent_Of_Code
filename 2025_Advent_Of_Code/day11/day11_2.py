server_rack = {}

with open("day11_test.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        key = parts[0][:-1]
        server_rack[key] = parts[1:]

print(server_rack)


def dfs(connection, visited):
    if connection == 'out':
        return int('fft' in visited and 'dac' in visited)

    paths = 0
    for cable in server_rack[connection]:
        if cable not in visited:
            visited.add(cable)
            paths += dfs(cable, visited)
            visited.remove(cable)

    return paths


connection = 'svr'
paths = dfs(connection, {'svr'})
print(paths)
