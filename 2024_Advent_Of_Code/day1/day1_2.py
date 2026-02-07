lst1 = []
frequency = {}

with open("day1_data.txt", "r") as lines:
    for line in lines:
        num1, num2 = map(int, line.split())
        lst1.append(num1)
        if num2 in frequency:
            frequency[num2] += 1
        else:
            frequency[num2] = 1

total = 0
for num in lst1:
    if num not in frequency:
        continue
    total += num * frequency[num]

print(total)
