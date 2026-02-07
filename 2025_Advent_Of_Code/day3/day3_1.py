file = open("day3_data.txt", "r")

total = 0
for line in file:
    maximum = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            maximum = max(maximum, int(line[i] + line[j]))
    total += maximum
print(total)
