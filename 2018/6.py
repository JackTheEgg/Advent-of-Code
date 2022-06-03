import numpy as np

coords = {}
with open("6.txt") as f:
	for i, line in enumerate(f):
		x, y = line.strip().split(", ")
		coords[i+1] = (int(x), int(y))

def isFinite(point, otherpoints):
	required = [(1,1), (1,-1), (-1,1), (-1,-1)]
	signs = set()
	for other in otherpoints:
		vector = (other[0] - point[0], other[1] - point[1])
		signs.add((np.sign(vector[0]), np.sign(vector[1])))
	for pair in required:
		if not pair in signs:
			return False
	return True

def scan(x, y, part2 = False):
    dists = {}
    for num, pos in coords.items():
        dists[num] = abs(pos[0] - x) + abs(pos[1] - y)
    if part2:
    	if sum(dists.values()) < 10000:
    		return True
    	else:
    		return False
    if list(dists.values()).count(min(dists.values())) > 1: return
    else:
        for num, dist in dists.items():
            if dist == min(dists.values()) and num in finite:
                finite[num] += 1 
                return

finite = {}
for point, coord in coords.items():
	otherpoints = [pair for pair in coords.values() if pair != coord]
	if isFinite(coord, otherpoints):
		finite[point] = 0

minX, maxX = min(i[0] for i in coords.values()), max(i[0] for i in coords.values())
minY, maxY = min(i[1] for i in coords.values()), max(i[1] for i in coords.values()) 

for y in range(minY, maxY + 1):
	for x in range(minX, maxX + 1):
		scan(x,y)
print(max(finite.values()))

size = 0
for y in range(minY, maxY + 1):
	for x in range(minX, maxX + 1):
		if scan(x,y,True):
			size += 1
print(size)