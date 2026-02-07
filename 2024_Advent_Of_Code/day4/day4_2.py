with open("day4_data.txt", "r") as lines:
    data = [[x for x in line.strip()] for line in lines]
print(data)


def search(row, col):
    total = 0
    # left or right
    if col - 1 > -1 and col + 1 < len(data[row]) and row - 1 > -1 and row + 1 < len(data):
        seq = (data[row - 1][col - 1] + data[row + 1][col - 1] +
               data[row - 1][col + 1] + data[row + 1][col + 1])
        if seq == 'MMSS' or seq == 'SSMM' or seq == 'MSMS' or seq == 'SMSM':
            total += 1
    return total


total = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'A':
            total += search(i, j)
print(total)
