file = open("day5_data.txt", "r")

ingredient_ranges = []
ingredient_ids = []
isBlankLine = False

for line in file:
    if line.startswith('\n'):
        isBlankLine = True
        continue
    line = line.replace("\n", "")
    if not isBlankLine:
        ingredient_ranges.append(line)
    else:
        ingredient_ids.append(int(line))


def strings_to_int_tuples(sorted_list):
    for i in range(len(sorted_list)):
        hyphen = sorted_list[i].index('-')
        sorted_list[i] = (int(sorted_list[i][:hyphen]), int(sorted_list[i][hyphen + 1:]))


def count_fresh_ids(ranges, ids):
    total = 0
    for i in ids:
        for r in ranges:
            if r[0] <= int(i) <= r[1]:
                total += 1
                break
    return total


sorted_ingredient_ranges = sorted(ingredient_ranges, key=lambda x: int(x.split('-')[0]))
strings_to_int_tuples(sorted_ingredient_ranges)
total_fresh_ids = count_fresh_ids(sorted_ingredient_ranges, ingredient_ids)
print(total_fresh_ids)
