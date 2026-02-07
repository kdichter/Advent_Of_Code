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
    visited = {update[-1]}
    i = len(update) - 2

    while i > -1:
        curr = update[i]
        for v in visited:
            if v not in pairs[update[i]]:
                j = update.index(v)
                update[i], update[j] = update[j], update[i]
                is_incorrect = True

                visited = {update[-1]}
                i = len(update) - 2
                break
        else:
            visited.add(curr)
            i -= 1
    return is_incorrect


total = 0
for update in updates_lst:
    if safe_update(update):
        total += int(update[len(update) // 2])
print(total)
