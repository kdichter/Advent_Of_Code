with open("day10_data.txt", "r") as file:
    machines = [line.strip().split(' ') for line in file]


# combination sum recursive
def backtrack(buttons, key, sequence, path, ret):
    if len(path) > len(sequence):
        return
    if sequence == key:
        ret.append(len(path))
        return
    for i in range(len(buttons)):
        new_sequence = press_buttons(sequence, buttons[i])
        backtrack(buttons[i:], key, new_sequence, path + [buttons[i]], ret)


# performs a combination sum on each of the different options
def fewest_presses(key, buttons):
    start = ['.'] * len(key)
    key = list(key)
    ret = []
    backtrack(buttons, key, start, [], ret)
    return min(ret)


def press_buttons(sequence, button):
    new_sequence = sequence.copy()
    button = button[1:len(button) - 1]
    nums = button.split(',')

    for num in nums:
        idx = int(num)
        new_sequence[idx] = '#' if new_sequence[idx] == '.' else '.'

    return new_sequence


total = 0
for machine in machines:
    key = machine[0][1:len(machine[0]) - 1]
    buttons = machine[1:len(machine) - 1]
    total += fewest_presses(key, buttons)

print(total)
