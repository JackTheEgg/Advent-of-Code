def genRow(row):
	nextRow = ""
	for i in range(len(row)):
		if i == 0:
			test = "." + row[:2]
		elif i == len(row) - 1:
			test = row[-2:] + "."
		else:
			test = row[i-1:i+2]
		if test == "^.." or test == "..^" or test == "^^." or test == ".^^":
			nextRow += "^"
		else:
			nextRow += "."
	return nextRow

grid = [open("18.txt").read().strip()]
for n in range(40 - 1):
	nextRow = genRow(grid[-1])
	grid.append(nextRow)
print(sum(grid[y][x] == "." for y in range(len(grid)) for x in range(len(grid[0]))))

grid = [open("18.txt").read().strip()]
for n in range(400000 - 1):
	nextRow = genRow(grid[-1])
	grid.append(nextRow)
print(sum(grid[y][x] == "." for y in range(len(grid)) for x in range(len(grid[0]))))