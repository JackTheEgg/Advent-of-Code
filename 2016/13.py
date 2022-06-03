def findSpot(x, y):
	val = x*x + 3*x + 2*x*y + y + y*y + num
	binary = str(format(val, "b"))
	if binary.count("1") % 2 == 0:
		return "."
	else:
		return "#"

num = int(open("13.txt").read().strip())
grid = [[" " for x in range(50)] for y in range(50)]

for y in range(len(grid)):
	for x in range(len(grid[0])):
		if x == 1 and y == 1:
			grid[y][x] = "S"
		elif x == 31 and y == 39:
			grid[y][x] = "E"
		else:
			grid[y][x] = findSpot(x, y)

grid.append(["#" for i in range(50)])
grid.insert(0, ["#" for i in range(50)])
for row in grid:
	row.append("#")
	row.insert(0, "#")

valid, endPoints, visited, paths = [], set(), set(), set()
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == ".":
			valid.append((x, y))
		elif grid[y][x] == "E":
			end = (x, y)
			valid.append((x, y))
		elif grid[y][x] == "S":
			startp1 = (x, y, 0)
			startp2 = (x, y)
			valid.append((x, y))

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def	genPaths(paths, addSteps = False):
	nextPaths = set()
	for path in paths:
		possible = set()
		for direct in dirs:
			if (path[0] + direct[0], path[1] + direct[1]) in valid and not (path[0] + direct[0], path[1] + direct[1]) in visited:
				if addSteps:
					possible.add((path[0] + direct[0], path[1] + direct[1], path[2] + 1))
				else:
					possible.add((path[0] + direct[0], path[1] + direct[1]))
		for mov in possible:
			nextPaths.add(mov)
			visited.add(mov)
	return nextPaths

visited.add(startp1)
paths.add(startp1)
stop = False

while True:
	if stop: break
	paths = genPaths(paths, True)
	for path in paths:
		if (path[0], path[1]) == end:
			print(path[2])
			stop = True
			break

visited, paths = set(), set()
visited.add(startp2)
paths.add(startp2)
visited.add(startp2)
endPoints.add(startp2)

for n in range(50):
	paths = genPaths(paths)
	for element in paths:
		endPoints.add(element)
print(len(endPoints))