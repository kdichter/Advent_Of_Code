file = open("day2_test.txt", "r")
data = ""
total = 0


def find_invalid_ids(f, s, t):
    for x in range(f, s + 1):
        str_x = str(x)
        middle = int(len(str_x) / 2)
        if int(len(str_x)) % 2 == 0 and str_x[0:middle] == str_x[middle:]:
            t += x
    return t


for line in file:
    data = line.split(',')
    for pair in data:
        nums = pair.split('-')
        first = int(nums[0])
        second = int(nums[1])
        total = find_invalid_ids(first, second, total)

print(total)
