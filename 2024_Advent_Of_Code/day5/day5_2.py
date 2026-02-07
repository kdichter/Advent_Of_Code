from collections import defaultdict

pairs = defaultdict(list)
updates_lst = []
with open("day5_data.txt", "r") as lines:
    data = lines.read()

rules, updates = data.split('\n\n')

for line in rules.splitlines():
    key, value = line.split('|')
    pairs[key].append(value)

print(pairs)

for line in updates.splitlines():
    updates_lst.append(line.strip().split(','))


def safe_update(update):
    is_incorrect = False
    visited = [update[-1]]
    i = len(update) - 2
    while i > -1:
        j = 0
        while j < len(visited):
            if visited[j] not in pairs[update[i]]:
                incorrect_idx = update.index(visited[j])
                update[i], update[incorrect_idx] = update[incorrect_idx], update[i]
                is_incorrect = True
                visited.clear()
                i = len(update) - 1
                break
            j += 1
        if update[i] not in visited:
            visited.append(update[i])
        i -= 1
    return is_incorrect


total = 0
for update in updates_lst:
    if safe_update(update):
        total += int(update[len(update) // 2])
print(total)
