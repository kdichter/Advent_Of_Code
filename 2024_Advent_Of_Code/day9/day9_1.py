data = []
idx_val = 0
idx = 0

with open("day9_data.txt", "r") as file:
    line = file.read()

while idx < len(line):
    if idx % 2 == 0:
        data.extend([idx_val] * int(line[idx]))
        idx_val += 1
    else:
        data.extend(['.'] * int(line[idx]))
    idx += 1

end_idx = len(data) - 1
swap_idx = data.index('.')
while end_idx > swap_idx:
    if data[end_idx] != '.':
        data[swap_idx], data[end_idx] = data[end_idx], data[swap_idx]
    swap_idx = data.index('.')
    end_idx -= 1

break_idx = data.index('.')
i = 1
total = 0
while i < break_idx:
    total += data[i] * i
    i += 1
print(total)
