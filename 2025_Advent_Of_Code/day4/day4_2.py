file = open("day4_data.txt", "r")
import time

start_time = time.time()
generation_total = -1
total = 0
forklift = []
generation = []
for line in file:
    line = line.replace("\n", "")
    forklift.append(line)

while generation_total != 0:
    generation_total = 0
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
                # forklift[i] = forklift[i][:j] + '.' + forklift[i][j + 1:]
                generation.append((i, j))
                generation_total += 1
                total += 1
    for k in generation:
        forklift[k[0]] = str(forklift[k[0]][:k[1]]) + '.' + str(forklift[k[0]][k[1] + 1:])
    generation = []
print(total)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
