with open("day12_data.txt", "r") as file:
    data = file.read().split('\n\n')[-1].splitlines()
    total = 0

    for d in data:
        grid, *presents = d.split(':')
        width, height = map(int, grid.split('x'))

        shapes = sum(list(map(int, presents[0].split())))

        mod = (width // 3) * (height // 3)
        if mod >= shapes:
            total += 1
print(total)
