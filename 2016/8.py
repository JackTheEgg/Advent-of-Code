import copy

grid = [[" " for x in range(50)] for y in range(6)]

with open("8.txt") as f:
	for line in f:
		grid2 = copy.deepcopy(grid)
		inp = line.strip().split(" ")
		if inp[0] == "rect":
			x, y = inp[1].split("x")
			for i in range(int(y)):
				for j in range(int(x)):
					grid2[i][j] = "#"
		elif inp[1] == "column":
			x = int(inp[2])
			for y in range(len(grid)):
				grid2[(y + int(inp[4])) % len(grid)][x] = grid[y][x]
		elif inp[1] == "row":
			y = int(inp[2])
			for x in range(len(grid[0])):
				grid2[y][(x + int(inp[4])) % len(grid[0])] = grid[y][x]
		grid = grid2
print(sum(grid[y][x] == "#" for y in range(6) for x in range(50)))

for row in grid:
	print("".join(row))