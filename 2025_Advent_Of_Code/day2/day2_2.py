file = open("day2_test.txt", "r")
data = ""
total = 0


def find_factors(num):
    lst = []
    for z in range(1, int(num / 2) + 1):
        if num % z == 0:
            lst.append(z)
    return lst


def is_invalid(string, fac):
    old = string[0:fac]
    i = fac
    while i < len(string) + 1 - fac:
        if old != string[i:i + fac]:
            return False
        i += fac
    return True


def find_invalid_ids(f, s, t):
    for x in range(f, s + 1):
        factors = find_factors(len(str(x)))
        for factor in factors:
            if is_invalid(str(x), factor):
                t += x
                break
    return t


for line in file:
    data = line.split(',')
    for pair in data:
        nums = pair.split('-')
        first = int(nums[0])
        second = int(nums[1])
        total = find_invalid_ids(first, second, total)

print(total)
