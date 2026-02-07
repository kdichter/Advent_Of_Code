file = open("day6_test.txt", "r")

data = []
total = 0

for line in file:
    data.append(line.split())
    # new_line = []
    # num = ''
    # for char in line:
    #     if char == ' ' or char == '\n':
    #         if num != '':
    #             new_line.append(num)
    #         num = ''
    #     else:
    #         num += char
    # data.append(new_line)

for col in range(len(data[0])):
    symbol = data[len(data) - 1][col]
    subtotal = 1 if symbol == '*' else 0
    for row in range(len(data) - 1):
        num = int(data[row][col])
        if symbol == '*':
            subtotal *= num
        else:
            subtotal += num
    total += subtotal

print(total)
print(data)
