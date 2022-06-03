dirs = open("1.txt").read().strip().split(", ")

turnR = {"N":"E", "E":"S", "S":"W", "W":"N"}
turnL = {v:k for k, v in turnR.items()}

x, y = 0, 0
face = "N"
for d in dirs:
	if d[0] == "L":
		face = turnL[face]
		if face == "E":
			x += int(d[1:])
		elif face == "W":
			x -= int(d[1:])
		elif face == "N":
			y += int(d[1:])
		elif face == "S":
			y -= int(d[1:])
	elif d[0] == "R":
		face = turnR[face]
		if face == "E":
			x += int(d[1:])
		elif face == "W":
			x -= int(d[1:])
		elif face == "N":
			y += int(d[1:])
		elif face == "S":
			y -= int(d[1:])
print(abs(x) + abs(y))

x, y = 0,0
visited = []
stop = False
for d in dirs:
	if stop: break
	if d[0] == "L":
		face = turnL[face]
		if face == "E":
			for i in range(int(d[1:])):
				x += 1
				if (x, y) in visited:
					print(abs(x) + abs(y))
					stop = True
					break
				visited.append((x, y))
		elif face == "W":
			for i in range(int(d[1:])):
				x -= 1
				if (x, y) in visited:
					print(abs(x) + abs(y))
					stop = True
					break
				visited.append((x, y))
		elif face == "N":
			for i in range(int(d[1:])):
				y += 1
				if (x, y) in visited:
					print(abs(x) + abs(y))
					stop = True
					break
				visited.append((x, y))		
		elif face == "S":
			for i in range(int(d[1:])):
				y -= 1
				if (x, y) in visited:
					print(abs(x) + abs(y))
					stop = True
					break
				visited.append((x, y))
	elif d[0] == "R":
		face = turnR[face]
		if face == "E":
			for i in range(int(d[1:])):
				x += 1
				if (x, y) in visited:
					print(abs(x) + abs(y))
					stop = True
					break
				visited.append((x, y))		
		elif face == "W":
			for i in range(int(d[1:])):
				x -= 1
				if (x, y) in visited:
					print(abs(x) + abs(y))
					stop = True
					break
				visited.append((x, y))		
		elif face == "N":
			for i in range(int(d[1:])):
				y += 1
				if (x, y) in visited:
					print(abs(x) + abs(y))
					stop = True
					break
				visited.append((x, y))		
		elif face == "S":
			for i in range(int(d[1:])):
				y -= 1
				if (x, y) in visited:
					print(abs(x) + abs(y))
					stop = True
					break
				visited.append((x, y))		