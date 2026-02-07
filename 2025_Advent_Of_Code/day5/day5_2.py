# file = open("day5_test.txt", "r")
file = open("day5_data.txt", "r")

ingredient_ranges = []
isBlankLine = False

for line in file:
    if line.startswith('\n'):
        isBlankLine = True
        continue
    line = line.replace("\n", "")
    if not isBlankLine:
        ingredient_ranges.append(line)
    else:
        break


def strings_to_lists(sorted_list):
    for i in range(len(sorted_list)):
        hyphen = sorted_list[i].index('-')
        sorted_list[i] = [int(sorted_list[i][:hyphen]), int(sorted_list[i][hyphen + 1:])]


def reduce_ranges(ranges):
    i = 1
    while i < len(ranges):
        if ranges[i][0] <= ranges[i - 1][1] + 1:
            ranges[i - 1][1] = max(ranges[i - 1][1], ranges[i][1])
            del ranges[i]
        else:
            i += 1


def count_fresh_ids(ranges):
    total = 0
    for r in ranges:
        total += (r[1] - r[0]) + 1
    return total


sorted_ingredient_ranges = sorted(ingredient_ranges, key=lambda x: int(x.split('-')[0]))
strings_to_lists(sorted_ingredient_ranges)
print(sorted_ingredient_ranges)
reduce_ranges(sorted_ingredient_ranges)
total_fresh_ids = count_fresh_ids(sorted_ingredient_ranges)

# 318140662027902

print(sorted_ingredient_ranges)
print(total_fresh_ids)
