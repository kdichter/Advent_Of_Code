from math import ceil, floor

file = open("day1_data.txt", "r")
dial = 50
password = 0

for line in file:
    num = int(line[1:])
    if line.startswith('L'):
        result = dial - num
        if num % 100 > dial != 0:
            password += ceil(num / 100)
        else:
            password += floor(num / 100)
    else:
        result = dial + num
        if num % 100 + dial > 100 != 0:
            password += ceil(num / 100)
        else:
            password += floor(num / 100)
    dial = result % 100
    if dial == 0:
        password += 1
print(password)
