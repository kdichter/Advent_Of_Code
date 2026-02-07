data = []

with open("day2_test.txt", "r") as lines:
    for line in lines:
        data.append(list(map(int, line.split())))

total = 0
isIncreasing = None
for i in range(len(data)):
    safe = True
    if data[i] == sorted(data[i]):
        isIncreasing = True
    elif data[i] == sorted(data[i], reverse=True):
        isIncreasing = False
    else:
        continue
    for j in range(len(data[i]) - 1):
        if isIncreasing:
            if not 1 <= data[i][j + 1] - data[i][j] <= 3:
                safe = False
                break
        else:
            if not 1 <= data[i][j] - data[i][j + 1] <= 3:
                safe = False
                break
    if safe:
        total += 1
print(total)
