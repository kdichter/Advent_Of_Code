file = open("day1_test.txt", "r")
dial = 50
password = 0

for line in file:
    if line.startswith('L'):
        dial = (dial - int(line[1:])) % 100
    else:
        dial = (dial + int(line[1:])) % 100
    if dial == 0:
        password += 1
print(password)
