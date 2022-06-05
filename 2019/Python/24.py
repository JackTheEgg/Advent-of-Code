from collections import defaultdict

grid, grid2 = {}, defaultdict(str) 
for y, line in enumerate(open("24.txt").readlines()):
	for x, c in enumerate(line.strip()):
		grid[(x,y)] = c
		grid2[(x, y, 0)] = c if c == "#" else ""
del grid2[(2,2,0)]
for x,y,level in list(grid2.keys()):
	for i in range(-150, 150):
		if i == 0:
			continue
		else:
			grid2[(x,y, level + i)] = ""

d = [(0,1), (0,-1), (1,0), (-1,0)]

def step(grid, part2 = False):
	if part2:
		newGrid = defaultdict(str)
		for x, y, level in list(grid.keys()):
			if (x,y) == (0,0): # esq sup izq (G)
				adj = [grid[(x+1, y, level)], grid[(x, y+1, level)], grid[(2, 1, level - 1)], grid[(1, 2, level - 1)]]
			elif (x,y) == (4,0): # esq sup dcha (G)
				adj = [grid[(x-1, y, level)], grid[(x, y+1, level)], grid[(2, 1, level - 1)], grid[(3, 2, level - 1)]]
			elif (x,y) == (4,4): # esq inf dcha (G)
				adj = [grid[(x-1, y, level)], grid[(x, y-1, level)], grid[(2, 3, level - 1)], grid[(3, 2, level - 1)]]
			elif (x,y) == (0,4): # esq inf izq (G)
				adj = [grid[(x+1, y, level)], grid[(x, y-1, level)], grid[(2, 3, level - 1)], grid[(1, 2, level - 1)]]
			elif (x,y) == (0,y): # vertical izq (G)
				adj = [grid[(x+1, y, level)], grid[(x, y-1, level)], grid[(x, y+1, level)], grid[(1, 2, level - 1)]]
			elif (x,y) == (4,y): # vertical dcha (G)
				adj = [grid[(x-1, y, level)], grid[(x, y-1, level)], grid[(x, y+1, level)], grid[(3, 2, level - 1)]]
			elif (x,y) == (x,0): # horiz sup (G)
				adj = [grid[(x-1, y, level)], grid[(x+1, y, level)], grid[(x, y+1, level)], grid[(2, 1, level - 1)]]
			elif (x,y) == (x,4): # horiz inf (G)
				adj = [grid[(x-1, y, level)], grid[(x+1, y, level)], grid[(x, y-1, level)], grid[(2, 3, level - 1)]]
			elif (x,y) == (2,1): # int sup (G)
				adj = [grid[(x-1, y, level)], grid[(x+1, y, level)], grid[(x, y-1, level)]] + [grid[(i, 0, level + 1)] for i in range(5)]
			elif (x,y) == (2,3): # int inf (G)
				adj = [grid[(x-1, y, level)], grid[(x+1, y, level)], grid[(x, y+1, level)]] + [grid[(i, 4, level + 1)] for i in range(5)]
			elif (x,y) == (1,2): # int izq (G)
				adj = [grid[(x-1, y, level)], grid[(x, y-1, level)], grid[(x, y+1, level)]] + [grid[(0, i, level + 1)] for i in range(5)]
			elif (x,y) == (3,2): # int dcha (G)
				adj = [grid[(x+1, y, level)], grid[(x, y-1, level)], grid[(x, y+1, level)]] + [grid[(4, i, level + 1)] for i in range(5)] 				
			else:
				adj = [grid[(x+dx, y+dy, level)] for dx, dy in d]
			if grid[(x,y,level)] == "#":
				if adj.count("#") == 1:
					newGrid[(x,y,level)] = "#"
				else:
					newGrid[(x,y,level)] = ""
			elif grid[(x,y,level)] == "":
				if adj.count("#") == 1 or adj.count("#") == 2:
					newGrid[(x,y,level)] = "#"
				else:
					newGrid[(x,y,level)] = ""
		return newGrid
	else:
		newGrid = {}
		for k in grid:
			adj = [grid[(k[0] + dx, k[1] + dy)] for dx, dy in d if grid.get((k[0] + dx, k[1] + dy))]
			if grid[k] == "#":
				if adj.count("#") == 1:
					newGrid[k] = "#"
				else:
					newGrid[k] = "."
			elif grid[k] == ".":
				if adj.count("#") == 1 or adj.count("#") == 2:
					newGrid[k] = "#"
				else:
					newGrid[k] = "."
		return newGrid

states = [grid]
while True:
	grid = step(grid)
	if grid in states:
		count = 0
		for i, k in enumerate(grid.keys()):
			if grid[k] == "#":
				count += 2 ** i
		print(count) 
		break
	states.append(grid)

for i in range(200):
	grid2 = step(grid2, True)
print(list(grid2.values()).count("#"))