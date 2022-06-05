import re

points = {}
with open("10.txt") as f:
	for i, line in enumerate(f):
		nums = list(map(int, re.findall("-?[0-9]+", line.strip())))
		points[i] = {"p":(nums[0], nums[1]), "v":(nums[2], nums[3])}

i = 0
while True:
	print(i)
	minX, maxX = min(v["p"][0] for v in points.values()), max(v["p"][0] for v in points.values())
	minY, maxY = min(v["p"][1] for v in points.values()), max(v["p"][1] for v in points.values())
	if maxX - minX <= 80:
		grid = []
		for y in range(minY, maxY + 1):
			row = ""
			for x in range(minX, maxX + 1):
				if (x,y) in (v["p"] for v in points.values()):
					row += "#"
				else:
					row += " "
			grid.append(row)
		for row in grid:
			print(row)
	for point, info in points.items():
		info["p"] = (info["p"][0] + info["v"][0], info["p"][1] + info["v"][1])
	i += 1