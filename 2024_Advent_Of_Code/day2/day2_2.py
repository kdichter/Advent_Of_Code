data = []

with open("day2_data.txt", "r") as lines:
    for line in lines:
        data.append(list(map(int, line.split())))


def is_safe(lst):
    if lst == sorted(lst):
        differences = [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]
    elif lst == sorted(lst, reverse=True):
        differences = [lst[i] - lst[i + 1] for i in range(len(lst) - 1)]
    else:
        return False
    return all(1 <= d <= 3 for d in differences)


safe_count = 0
for lst in data:
    if is_safe(lst):
        safe_count += 1
    else:
        for i in range(len(lst)):
            new_lst = lst[:i] + lst[i + 1:]
            if is_safe(new_lst):
                safe_count += 1
                break

print(safe_count)
