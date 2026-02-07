import re

with open("day13_data.txt", "r") as file:
    machines = file.read().split('\n\n')

total = 0
for machine in machines:
    ax, ay, bx, by, px, py = map(int, re.findall(r'\d+', machine))
    px += 10000000000000
    py += 10000000000000
    s = (px * by - py * bx) / (ax * by - ay * bx)
    t = (px - ax * s) / bx
    if s % 1 == 0 and t % 1 == 0:
        total += int(s * 3 + t)
print(total)
