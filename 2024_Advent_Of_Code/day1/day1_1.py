lst1 = []
lst2 = []

with open("day1_data.txt", "r") as lines:
    # data = file.read().split('\n')
    for line in lines:
        num1, num2 = map(int, line.split())
        lst1.append(num1)
        lst2.append(num2)

lst1.sort()
lst2.sort()

total = 0
for i in range(len(lst1)):
    total += abs(lst1[i] - lst2[i])
print(total)
