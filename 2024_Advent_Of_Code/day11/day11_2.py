from collections import Counter

with open("day11_data.txt", "r") as file:
    stones = [int(x) for x in file.read().split()]


def count_stones(data, blinks):
    counter = Counter(data)

    for i in range(blinks):
        new_counter = Counter()
        for stone, count in counter.items():
            if stone == 0:
                new_counter[1] += count
                continue

            string = str(stone)
            length = len(string)
            if length % 2 == 0:
                mid = length // 2
                new_counter[int(string[:mid])] += count
                new_counter[int(string[mid:])] += count
            else:
                new_counter[stone * 2024] += count

        counter = new_counter
    return sum(counter.values())


print(count_stones(stones, 75))
