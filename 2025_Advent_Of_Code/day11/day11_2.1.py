from functools import cache

server_rack = {}

with open("day11_test.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        key = parts[0][:-1]
        server_rack[key] = parts[1:]

print(server_rack)


@cache
def count(src, dst):
    if src == dst:
        return 1
    return sum(count(x, dst) for x in server_rack.get(src, []))


print(count('svr', 'dac') * count('dac', 'fft') * count('fft', 'out')
      + count('svr', 'fft') * count('fft', 'dac') * count('dac', 'out'))
