total = 0
isEnabled = True


def find_do(line):
    try:
        do_idx = line.index('do()')
        return do_idx
    except ValueError:
        return -1


def find_dont(line):
    try:
        dont_idx = line.index('don\'t()')
        return dont_idx
    except ValueError:
        return -1


with open("day3_data.txt", "r") as lines:
    for line in lines:
        while True:
            try:
                do_idx = find_do(line)
                dont_idx = find_dont(line)
                mul_idx = line.index('mul(')

                if do_idx != -1 and dont_idx != -1:
                    if dont_idx < do_idx < mul_idx:
                        isEnabled = True
                    elif do_idx < dont_idx < mul_idx:
                        isEnabled = False
                if do_idx != -1 and do_idx < mul_idx:
                    isEnabled = True
                elif dont_idx != -1 and dont_idx < mul_idx:
                    isEnabled = False

                line = line[mul_idx + 4:]

                if isEnabled:
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
