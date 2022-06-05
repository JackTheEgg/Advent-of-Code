inp = open("3.txt").read().strip()
houses, x, y = set(), 0, 0
houses.add((0,0))

for char in inp:
	if char == "^":
		y += 1
		houses.add((x,y))
	elif char == "v":
		y -= 1
		houses.add((x,y))
	elif char == ">":
		x += 1
		houses.add((x,y))
	elif char == "<":
		x -= 1
		houses.add((x,y))
print(len(houses))

houses, sanX, sanY, robX, robY = set(), 0, 0, 0, 0
houses.add((0,0))
for ind, char in enumerate(inp):
	if char == "^":
		if ind % 2 == 0:
			sanY += 1
			houses.add((sanX, sanY))
		else:
			robY += 1
			houses.add((robX, robY))
	elif char == "v":
		if ind % 2 == 0:
			sanY -= 1
			houses.add((sanX, sanY))
		else:
			robY -= 1
			houses.add((robX, robY))
	elif char == ">":
		if ind % 2 == 0:
			sanX += 1
			houses.add((sanX, sanY))
		else:
			robX += 1
			houses.add((robX, robY))
	elif char == "<":
		if ind % 2 == 0:
			sanX -= 1
			houses.add((sanX, sanY))
		else:
			robX -= 1
			houses.add((robX, robY))
print(len(houses))