file = open("day3_data.txt", "r")

total = 0
jolt_length = 12


def largest_jolts(string: str):
    stack = []
    idx = 0
    while idx < len(string):
        digit = int(string[idx])
        if len(stack) == 0:
            stack.append(digit)
        else:
            while len(stack) > 0:
                value = stack[len(stack) - 1]
                if digit > value and len(stack) + (len(string) - idx - 1) >= jolt_length:
                    stack.pop()
                else:
                    if len(stack) < 12:
                        stack.append(digit)
                    break
            if len(stack) == 0:
                stack.append(digit)
        idx += 1
    return ''.join(str(i) for i in stack)


for line in file:
    line = line.replace("\n", "")
    maximum = largest_jolts(line)
    print(maximum)
    total += int(maximum)
print(total)
