def hexagons(steps):
	if steps == 0:
		return [(0,0)]
	else:
		points = []
		x, y = 0, 2*steps
		for mov in movs:
			for n in range(steps):
				x += mov[0]
				y += mov[1]
				points.append((x, y))
		return points

path = open("11.txt").read().strip().split(",")
movs = [(1,-1), (0,-2), (-1,-1), (-1,1), (0,2), (1,1)]

x, y, visited = 0, 0, set()
for step in path:
	if step == "n":
		y += 2
		visited.add((x,y))
	elif step == "ne":
		y += 1
		x += 1
		visited.add((x,y))
	elif step == "nw":
		y += 1
		x -= 1
		visited.add((x,y))
	elif step == "se":
		y -= 1
		x += 1
		visited.add((x,y))
	elif step == "sw":
		y -= 1
		x -= 1
		visited.add((x,y))
	elif step == "s":
		y -= 2
		visited.add((x,y))

steps = 1
while True:
	points = hexagons(steps)
	if (x,y) in points:
		print(steps)
		break
	steps += 1

steps = []
step = 1
while True:
	found = False
	points = hexagons(step)
	for point in points:
		if point in visited:
			steps.append(step)
			step += 1
			found = True
			break
	if not found:
		break
print(max(steps))