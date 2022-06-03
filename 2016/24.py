from itertools import permutations

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
			if (mov[0], mov[1]) in numcoords:
				numdists[num][numcoords[(mov[0], mov[1])]] = mov[2]
				visited.add((mov[0], mov[1]))
			else:
				nextPaths.add(mov)
				visited.add((mov[0], mov[1]))
	return nextPaths

inp = open("24.txt").readlines()

valid, numcoords, nums = [], {}, [str(i) for i in range(8)]
for y, line in enumerate(inp):
	for x, char in enumerate(line.strip()):
		if char == " ":
			valid.append((x, y))
		elif char in nums:
			numcoords[(x, y)] = char
			valid.append((x, y))

numdists = {str(i):{} for i in range(8)}
for pos, num in numcoords.items():
	visited = set()
	paths = set()
	paths.add((pos[0], pos[1], 0))
	visited.add((pos[0], pos[1]))
	while len(paths) != 0:
		paths = genPaths(paths, True)

ways = list(permutations([str(i) for i in range(1,8)]))
dists = []
for way in ways:
	dist = 0
	way = list(way)
	way.insert(0, "0")
	for i in range(0, len(way) - 1):
		dist += numdists[way[i]][way[i+1]]
	dists.append(dist)
print(min(dists))

dists = []
for way in ways:
	dist = 0
	way = list(way)
	way.insert(0, "0")
	way.append("0")
	for i in range(0, len(way) - 1):
		dist += numdists[way[i]][way[i+1]]
	dists.append(dist)
print(min(dists))