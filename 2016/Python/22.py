import re

nodes = {}
with open("22.txt") as f:
	for line in f:
		nums = list(map(int, re.findall("-?[0-9]+", line.strip()))) # x, y, Size, Use, Avail, Use%
		nodes[(nums[0], nums[1])] = {"Size": nums[2], "Use": nums[3], "Avail": nums[4], "Use%": nums[5]}

coords = list(nodes.keys())
viable = 0
for i in range(len(coords)):
    coord = coords[i]
    if nodes[coord]["Use"] == 0:
    	continue
    othercoords = [x for n, x in enumerate(coords) if n != i]
    for pair in othercoords:
    	if nodes[coord]["Use"] <= nodes[pair]["Avail"]:
    		viable += 1
print(viable)

grid = []
for y in range(max(coord[1] for coord in coords) + 1):
	row = ""
	for x in range(max(coord[0] for coord in coords) + 1):
		if nodes[(x, y)]["Use%"] == 0:
			row += "_"
		elif nodes[(x, y)]["Size"] > 100:
			row += "|"
		elif x == 0 and y == 0:
			row += "G"
		elif x == max(coord[0] for coord in coords) and y == 0:
			row += "S"
		else:
			row += "."
	grid.append(row)
print(33*5 + 57) # Para mover _ hasta S necesitas 57 pasos y luego (34 - 1) * 5