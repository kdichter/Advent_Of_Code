from collections import defaultdict

pairs = defaultdict(list)
updates_lst = []
with open("day5_test.txt", "r") as lines:
    data = lines.read()

rules, updates = data.split('\n\n')

for line in rules.splitlines():
    key, value = line.split('|')
    pairs[key].append(value)

print(pairs)

for line in updates.splitlines():
    updates_lst.append(line.strip().split(','))


def safe_update(update):
    visited = [update[-1]]
    for i in range(len(update) - 2, -1, -1):
        for j in range(len(visited)):
            if visited[j] not in pairs[update[i]]:
                return False
        visited.append(update[i])
    return True


total = 0
for update in updates_lst:
    if safe_update(update):
        total += int(update[len(update) // 2])
print(total)
