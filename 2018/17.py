import re

def printGrid():
	for y in range(minY, maxY + 1):
		row = ""
		for x in range(minX - 5, maxX + 5):
			if (x,y) in clay:
				row += "#"
			elif (x,y) in sWater:
				row += "~"
			elif (x,y) in water:
				row += "|"
			else:
				row += " "
		print(row)

clay = set()
with open("17.txt") as f:
	for line in f:
		nums = list(map(int, re.findall("-?[0-9]+", line.strip())))
		if line[0] == "x":
			for y in range(nums[1], nums[2] + 1):
				clay.add((nums[0], y))
		elif line[0] == "y":
			for x in range(nums[1], nums[2] + 1):
				clay.add((x, nums[0]))
minX, maxX = min(c[0] for c in clay), max(c[0] for c in clay)
minY, maxY = min(c[1] for c in clay), max(c[1] for c in clay)

def fill(p):
	if p in sWater: return fill((p[0], p[1] - 1))
	sL, sR, filled, flows = False, False, set(), set()
	filled.add(p)
	water.add(p)
	for i in range(1, 1000):
		if sR and sL:
			if len(flows) > 0:
				return flows
			else:
				sWater.update(filled)
				return fill((p[0], p[1] - 1))
		if not sR:
			if (p[0] + i, p[1]) not in clay:
				water.add((p[0] + i, p[1]))
				filled.add((p[0] + i, p[1]))
				if (p[0] + i, p[1] + 1) not in clay and (p[0] + i, p[1] + 1) not in sWater:
					flows.add((p[0] + i, p[1]))
					sR = True
			else:
				sR = True
		if not sL:
			if (p[0] - i, p[1]) not in clay:
				water.add((p[0] - i, p[1]))				
				filled.add((p[0] - i, p[1]))
				if (p[0] - i, p[1] + 1) not in clay and (p[0] - i, p[1] + 1) not in sWater:
					flows.add((p[0] - i, p[1]))
					sL = True
			else:
				sL = True

def getFlow(flow):
	newFlow = set()
	for f in flow:
		if (f[0], f[1] + 1) not in clay and (f[0], f[1] + 1) not in sWater and f[1] <= maxY:
			water.add(f)
			newFlow.add((f[0], f[1] + 1))
		elif f[1] <= maxY:
			newFlow.update(fill(f))
	return newFlow

sWater, water, flow = set(), set(), set()
flow.add((500,0))
while len(flow) > 0:
	flow = getFlow(flow)

print(len([w for w in water | sWater if minY <= w[1] <= maxY]))
print(len([w for w in sWater if minY <= w[1] <= maxY]))