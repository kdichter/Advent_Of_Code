total = 0
with open("day3_data.txt", "r") as lines:
    for line in lines:
        while True:
            try:
                mul_start = line.index('mul(')
                line = line[mul_start + 4:]
                paren_end = line.index(')')
                content = line[:paren_end]
                parts = content.split(',')
                if len(parts) == 2:
                    num1, num2 = parts
                    if num1.isdigit() and num2.isdigit():
                        total += int(num1) * int(num2)
            except ValueError:
                break
    print(total)
