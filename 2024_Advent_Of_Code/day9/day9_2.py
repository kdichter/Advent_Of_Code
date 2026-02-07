data = []
idx_val = 0
idx = 0

with open("day9_data.txt", "r") as file:
    line = file.read()

while idx < len(line):
    if idx % 2 == 0:
        data.append([idx_val, int(line[idx])])
        idx_val += 1
    else:
        data.append(['.', int(line[idx])])
    idx += 1
# print(data)

end_idx = len(data) - 1
while end_idx >= 0:
    if data[end_idx][0] != '.':
        dot_indices = [i for i, [val, n] in enumerate(data[:end_idx]) if val == '.' and n > 0]
        num = data[end_idx][1]
        for dot_index in dot_indices:
            if num <= data[dot_index][1]:
                data[dot_index][1] -= num
                moved_item = data[end_idx][:]
                data.insert(dot_index, moved_item)
                data[end_idx + 1][0] = '.'
                break
    end_idx -= 1

# print(data)

i = 0
total = 0

for val, n in data:
    if val == '.':
        i += n
    else:
        for _ in range(n):
            total += val * i
            i += 1

print(total)
