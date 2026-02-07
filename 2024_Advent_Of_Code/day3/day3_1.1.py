import re

total = 0
with open("day3_data.txt", "r") as f:
    text = f.read()

    # Find all valid mul(X,Y) where X and Y are 1-3 digit numbers
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, text)

    for num1, num2 in matches:
        total += int(num1) * int(num2)

print(total)
