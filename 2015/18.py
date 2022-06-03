import copy

grid = []
with open("18.txt") as f:
	for line in f:
		row = []
		for char in line.strip():
			row.append(char)
		grid.append(row)

gridp2 = copy.deepcopy(grid)
gridp2[1][1] = "#"
gridp2[1][len(gridp2[0]) - 2] = "#"
gridp2[len(gridp2) - 2][1] = "#"
gridp2[len(gridp2) - 2][len(gridp2[0]) - 2] = "#"

for n in range(100):
	grid2 = copy.deepcopy(grid)
	for y in range(1, len(grid) - 1):
		for x in range(1, len(grid[0]) - 1):
			if grid[y][x] == "#":
				if (sum(grid[y+i][x+j] == "#" for i in range(-1, 2) for j in range(-1, 2)) - 1) == 2 or (sum(grid[y+i][x+j] == "#" for i in range(-1, 2) for j in range(-1, 2)) - 1) == 3:
					grid2[y][x] = "#"
				else:
					grid2[y][x] = "."
			elif grid[y][x] == ".":
				if sum(grid[y+i][x+j] == "#" for i in range(-1, 2) for j in range(-1, 2)) == 3:
					grid2[y][x] = "#"
				else:
					grid2[y][x] = "."
	grid = grid2
print(sum(grid[y][x] == "#" for y in range(len(grid)) for x in range(len(grid[0]))))

for n in range(100):
	grid2 = copy.deepcopy(gridp2)
	for y in range(1, len(gridp2) - 1):
		for x in range(1, len(gridp2[0]) - 1):
			if (y == 1 and x == 1) or (y == 1 and x == len(gridp2[0]) - 2) or (y == len(gridp2) - 2 and x == 1) or (y == len(gridp2) - 2 and x == len(gridp2[0]) - 2):
				continue
			if gridp2[y][x] == "#":
				if (sum(gridp2[y+i][x+j] == "#" for i in range(-1, 2) for j in range(-1, 2)) - 1) == 2 or (sum(gridp2[y+i][x+j] == "#" for i in range(-1, 2) for j in range(-1, 2)) - 1) == 3:
					grid2[y][x] = "#"
				else:
					grid2[y][x] = "."
			elif gridp2[y][x] == ".":
				if sum(gridp2[y+i][x+j] == "#" for i in range(-1, 2) for j in range(-1, 2)) == 3:
					grid2[y][x] = "#"
				else:
					grid2[y][x] = "."
	gridp2 = grid2
print(sum(gridp2[y][x] == "#" for y in range(len(gridp2)) for x in range(len(gridp2[0]))))