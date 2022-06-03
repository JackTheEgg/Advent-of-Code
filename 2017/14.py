from functools import reduce
from operator import xor

def step(lst, size, i, skipSize):
	L = len(lst)
	frag = [lst[(i + n) % L] for n in range(size)]
	frag.reverse()
	for n in range(size):
		lst[(i + n) % L] = frag[n]
	i += (size + skipSize) % L 
	skipSize += 1
	return lst, i, skipSize

grid = []
for n in range(128):
	lst = [i for i in range(256)]
	inp = open("14.txt").read().strip() + "-" + str(n)
	seq = [ord(char) for char in inp] + [17, 31, 73, 47, 23]
	i, skipSize = 0, 0
	for a in range(64):
		for num in seq:
			lst, i, skipSize = step(lst, num, i, skipSize)
	dHash = []
	for i in range(0, len(lst), 16):
		dHash.append(reduce(xor, lst[i:i+16]))
	s = ""
	for num in dHash:
		h = hex(num)[2:]
		if len(h) == 1:
			s += "0" + h
		else:
			s += h
	b = "".join([bin(int(char, 16))[2:].zfill(4) for char in s])
	grid.append(b)

count = 0
for row in grid:
	count += row.count("1")
print(count)

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
def	genPaths(paths, group, addSteps = False):
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
			groups[group].append(mov)
			nextPaths.add(mov)
			visited.add((mov[0], mov[1]))
	return nextPaths

valid, visited = set(), set()
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == "1":
			valid.add((x, y))

groups = {}
group = 0
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if (x, y) in valid and not (x, y) in visited:
			group += 1
			groups[group] = [(x,y)]
			paths = set()
			paths.add((x, y))
			visited.add((x, y))
			while len(paths) != 0:
				paths = genPaths(paths, group)
print(len(groups))