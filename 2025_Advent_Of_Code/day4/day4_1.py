file = open("day4_data.txt", "r")

total = 0
forklift = []
line_length = 0
for line in file:
    line = line.replace("\n", "")
    forklift.append(line)

for i in range(len(forklift)):
    for j in range(len(forklift[i])):
        if forklift[i][j] == '.':
            continue
        count = 0
        # above
        if i > 0:
            if forklift[i - 1][j] == '@':
                count += 1
        # below
        if i < len(forklift) - 1:
            if forklift[i + 1][j] == '@':
                count += 1
        # left
        if j > 0:
            if forklift[i][j - 1] == '@':
                count += 1
        # right
        if j < len(forklift[i]) - 1:
            if forklift[i][j + 1] == '@':
                count += 1
        # top left
        if i > 0 and j > 0:
            if forklift[i - 1][j - 1] == '@':
                count += 1
        # top right
        if i > 0 and j < len(forklift[i]) - 1:
            if forklift[i - 1][j + 1] == '@':
                count += 1
        # bottom left
        if i < len(forklift) - 1 and j > 0:
            if forklift[i + 1][j - 1] == '@':
                count += 1
        # bottom right
        if i < len(forklift) - 1 and j < len(forklift[i]) - 1:
            if forklift[i + 1][j + 1] == '@':
                count += 1
        if count < 4:
            total += 1

print(total)
