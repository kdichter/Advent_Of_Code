grid = [list(line.strip()) for line in open("day7_test.txt", "r")]

S = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "S"][0]

print(*S)
