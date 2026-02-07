with open("day11_data.txt", "r") as file:
    stones = [int(x) for x in file.read().split()]

data_cache = {}


def count_stones(data, blinks):
    for i in range(blinks):
        stones = []
        for stone in data:
            string = str(stone)
            length = len(string)

            if stone in data_cache:
                if length % 2 == 0:
                    stones.append(data_cache[stone][1])
                    stones.append(data_cache[stone][0])
                else:
                    stones.append(data_cache[stone])
            else:
                if stone == 0:
                    stones.append(1)
                    data_cache[stone] = stones[-1]
                elif length % 2 == 0:
                    mid = length // 2
                    stones.append(int(string[:mid]))
                    stones.append(int(string[mid:]))
                    data_cache[stone] = stones[-2], stones[-1]
                else:
                    stones.append(stone * 2024)
                    data_cache[stone] = stones[-1]
        data = stones
    return len(stones)


print(count_stones(stones, 25))
