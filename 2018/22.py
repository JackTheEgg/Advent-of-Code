from heapq import heappush, heappop

with open("22.txt") as f:
	for i, line in enumerate(f):
		if i == 0:
			depth = int(line.strip().split()[1])
		else:
			a = line.strip().split(": ")
			endX, endY = int(a[1].split(",")[0]), int(a[1].split(",")[1])

def getErosion(x, y):
	GI = None
	if x == y == 0 or (x == endX and y == endY):
		GI = 0
	elif y == 0:
		GI = x * 16807
	elif x == 0:
		GI = y * 48271
	else:
		GI = erosions[(x - 1, y)] * erosions[(x, y - 1)]
	erosion = (GI + depth) % 20183
	return erosion

erosions = {}
grid = {}
count = 0
for y in range(endY + 1000):
	for x in range(endX + 1000):
		erosion = getErosion(x, y)
		erosions[(x,y)] = erosion
		grid[(x,y)] = erosions[(x,y)] % 3
		if x <= endX and y <= endY:
			count += erosion % 3
print(count)

Q = [(0,0,0,1)] # ind, x, y, item
bestTimes = {}
target = (endX, endY, 1)
while Q:
	time, x, y, item = heappop(Q)
	best = (x, y, item)
	if best in bestTimes and bestTimes[best] <= time:
		continue
	bestTimes[best] = time 
	if best == target:
		print(time)
		break
	for i in range(3):
		if i != item and i != grid[(x,y)]:
			heappush(Q, (time + 7, x, y, i))
	for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
		newx = x + dx
		newy = y + dy
		if newx < 0:
			continue
		if newy < 0:
			continue
		if grid[(newx, newy)] == item:
			continue
		heappush(Q, (time + 1, newx, newy, item))
# 1015