data = []
with open("day7_data.txt", "r") as lines:
    for line in lines:
        left, right = line.strip().split(': ')
        data.append((int(left), [int(x) for x in right.split()]))


def is_valid(target, nums, curr, idx):
    if curr > target:
        return False
    if idx == len(nums):
        return curr == target
    return (is_valid(target, nums, curr + nums[idx], idx + 1) or
            is_valid(target, nums, curr * nums[idx], idx + 1) or
            is_valid(target, nums, int(str(curr) + str(nums[idx])), idx + 1))


total = 0
for pair in data:
    if is_valid(pair[0], pair[1], pair[1][0], 1):
        total += pair[0]
print(total)
