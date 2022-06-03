grid = []
with open("22.txt") as f:
	for line in f:
		grid.append(line.strip())

infected = set()
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == "#":
			infected.add((x,y))

turnR = {"U":"R", "R":"D", "D":"L", "L":"U"}
turnL = {v:k for k, v in turnR.items()}
turnO = {"U":"D", "D":"U", "L":"R", "R":"L"}
move = {"U":(0,-1), "D":(0,1), "L":(-1,0), "R":(1,0)}
face = "U"
x, y = len(grid[0]) // 2, len(grid) // 2

count = 0
for i in range(10000):
	if (x,y) in infected:
		face = turnR[face]
	else:
		face = turnL[face]
	if not (x,y) in infected:
		infected.add((x,y))
		count += 1
	else:
		infected.remove((x,y))
	x += move[face][0]
	y += move[face][1]
print(count)

infected = set()
for y in range(len(grid)):
	for x in range(len(grid[0])):
		if grid[y][x] == "#":
			infected.add((x,y))

flagged = set()
weakened = set()
face = "U"
x, y = len(grid[0]) // 2, len(grid) // 2

count = 0
for i in range(10000000):
	if (x,y) in weakened:
		face = face
	elif (x,y) in infected:
		face = turnR[face]
	elif (x,y) in flagged:
		face = turnO[face]
	else:
		face = turnL[face]
	if (x,y) in weakened:
		infected.add((x,y))
		weakened.remove((x,y))
		count += 1
	elif (x,y) in infected:
		flagged.add((x,y))
		infected.remove((x,y))
	elif (x,y) in flagged:
		flagged.remove((x,y))
	else:
		weakened.add((x,y))
	x += move[face][0]
	y += move[face][1]
print(count)