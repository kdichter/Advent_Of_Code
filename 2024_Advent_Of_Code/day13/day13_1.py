import re

with open("day13_data.txt", "r") as file:
    machines = [line.split('\n') for line in file.read().split('\n\n')]


def tokens(a, b, p):
    for i in range(100, -1, - 1):
        if i * b[0] <= p[0] and i * b[1] <= p[1]:
            x_remain = p[0] - i * b[0]
            y_remain = p[1] - i * b[1]
            if x_remain % a[0] == 0 and y_remain % a[1] == 0:
                a_x = x_remain / a[0]
                a_y = y_remain / a[1]
                if a_x == a_y and a_x <= 100 and a_y <= 100:
                    return int(a_x) * 3, i
    return -1, -1


total = 0
for machine in machines:
    pairs = [tuple(map(int, re.findall(r'\d+', s))) for s in machine]
    a = pairs[0]
    b = pairs[1]
    p = pairs[2]
    token_pair = tokens(a, b, p)
    if token_pair[0] > -1:
        total += token_pair[0] + token_pair[1]
print(total)
