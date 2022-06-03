grid = []
with open("15b.txt") as f:
	for line in f:
		grid.append(line.strip())

valid, visited, start, oxygen = [], [], "", ""
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == " ":
			valid.append((x, y))
		elif grid[y][x] == "O":
			oxygen = (x, y)
			valid.append((x, y))
		elif grid[y][x] == "S":
			start = (x, y)
			valid.append((x, y))
visited.append(start)

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
paths = [[start, 0]]
stop = False
while True:
	if stop: break
	for path in paths:
		valids = []
		for mov in dirs:
			if (path[0][0] + mov[0], path[0][1] + mov[1]) in valid and not (path[0][0] + mov[0], path[0][1] + mov[1]) in visited:
				valids.append((path[0][0] + mov[0], path[0][1] + mov[1]))
		if len(valids) == 0: continue
		else:
			path[0] = valids[0]
			path[1] += 1
			visited.append(valids[0])
			if len(valids) > 1:
				for item in valids[1:]:
					paths.append([item, path[1]])
					visited.append(item)
		if path[0] == oxygen:
			stop = True
			break
for item in paths:
	if item[0] == oxygen:
		print(item[1])

valid.remove(oxygen)
visited, paths = [oxygen], [[oxygen]]
count = 0
while len(valid) > 0:
	newPath = []
	count += 1
	for path in paths:
		valids = []
		for mov in dirs:
			if (path[0][0] + mov[0], path[0][1] + mov[1]) in valid and not (path[0][0] + mov[0], path[0][1] + mov[1]) in visited:
				valids.append((path[0][0] + mov[0], path[0][1] + mov[1]))
		if len(valids) == 0: continue
		else:
			newPath.append([valids[0]])
			visited.append(valids[0])
			valid.remove(valids[0])
			if len(valids) > 1:
				for item in valids[1:]:
					newPath.append([item])
					visited.append(item)		
					valid.remove(item)
	paths = newPath.copy()
print(count)