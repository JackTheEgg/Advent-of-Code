grid = []
with open("19.txt") as f:
	for line in f:
		row = [char for char in line.rstrip("\n")]
		grid.append(row)

y = 0
for ind, char in enumerate(grid[0]):
	if char == "|":
		x = ind
		break

face = "D"
s = ""
steps = 1
while True:
	while not (grid[y][x] == "+" or grid[y][x] == " "):
		if grid[y][x].isupper():
			s += grid[y][x]
		if face == "D":
			y += 1
			steps += 1
		elif face == "U":
			y -= 1
			steps += 1
		elif face == "L":
			x -= 1
			steps += 1
		elif face == "R":
			x += 1
			steps += 1
	if grid[y][x] == " ":
		break
	elif grid[y][x] == "+":
		if face == "D" or face == "U":
			if grid[y][x-1] != " ":
				face = "L"
				x -= 1
				steps += 1
			else:
				face = "R"
				x += 1
				steps += 1
		elif face == "R" or face == "L":
			if grid[y-1][x] != " ":
				face = "U"
				y -= 1
				steps += 1
			else:
				face = "D"
				y += 1
				steps += 1
print(s)
print(steps - 1)