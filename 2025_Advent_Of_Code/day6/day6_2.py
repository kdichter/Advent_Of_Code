file = open("day6_test.txt", "r")

data = []
max_line_length = 0
total = 0

for line in file:
    max_line_length = max(len(line), max_line_length)
    curr_length = len(line)
    while curr_length < max_line_length:
        line += ' '
        curr_length += 1
    data.append(line)

idx = 0
symbol = ''
subtotal = 0
for col in range(len(data[0])):
    temp_symbol = data[len(data) - 1][idx]
    if temp_symbol != ' ':
        total += subtotal
        symbol = data[len(data) - 1][idx]
        subtotal = 1 if symbol == '*' else 0
    num = ''
    for row in range(len(data) - 1):
        val = data[row][col]
        num += val
    if num.strip() != '':
        if symbol == '*':
            subtotal *= int(num)
        else:
            subtotal += int(num)
    idx += 1

total += subtotal
print(total)
print(data)
