from collections import deque, defaultdict

valid, portals, start, end = {}, defaultdict(list), None, None
inp = [line.rstrip("\n") for line in open("20.txt").readlines()]
for y, line in enumerate(inp):
	for x, c in enumerate(line):
		if x == 0 or y == 0 or x == len(line) - 1 or y == len(inp) - 1:
			continue
		if c == ".":
			valid[(x,y)] = True
		elif c.isupper():
			sV, sH = inp[y-1][x] + c + inp[y+1][x], inp[y][x-1] + c + inp[y][x+1]
			if "AA" in sV and "." in sV:
				if sV[0] == ".":
					start = (x, y-1)
				else:
					start = (x, y+1)
			elif "AA" in sH and "." in sH:
				if sH[0] == ".":
					start = (x-1, y)
				else:
					start = (x+1, y)
			elif "ZZ" in sV and "." in sV:
				if sV[0] == ".":
					end = (x, y-1)
				else:
					end = (x, y+1)
			elif "ZZ" in sH and "." in sH:
				if sH[0] == ".":
					end = (x-1, y)
				else:
					end = (x+1, y)
			elif sum(1 for c in sV if c.isupper()) == 2 and "." in sV:
				if sV[0] == ".":
					portals[sV[1:]].append((x,y-1))
				else:
					portals[sV[:-1]].append((x,y+1))
			elif sum(1 for c in sH if c.isupper()) == 2 and "." in sH:
				if sH[0] == ".":
					portals[sH[1:]].append((x-1,y))
				else:
					portals[sH[:-1]].append((x+1,y))
pairs, inner, outer = {}, set(), set()
for _, v in portals.items():
	if v[0][0] == 2 or v[0][0] == len(inp[0]) - 3 or v[0][1] == 2 or v[0][1] == len(inp) - 3:
		outer.add(v[0])
	else:
		inner.add(v[0])
	if v[1][0] == 2 or v[1][0] == len(inp[0]) - 3 or v[1][1] == 2 or v[1][1] == len(inp) - 3:
		outer.add(v[1])
	else:
		inner.add(v[1])
	pairs[v[0]] = v[1]
	pairs[v[1]] = v[0]

dirs = [(0,1), (0,-1), (1,0), (-1,0)]
Q = deque([(start[0], start[1], 0, {start:True})])
while Q:
	x, y, steps, visited = Q.popleft()
	for dx, dy in dirs:
		if (x + dx, y + dy) == end:
			print(steps + 1)
			Q.clear()
			break
		if visited.get((x + dx, y + dy)):
			continue
		elif pairs.get((x + dx, y + dy)):
			visited[(x + dx, y + dy)] = True
			visited[pairs[(x + dx, y + dy)]] = True
			Q.append((pairs[(x + dx, y + dy)][0], pairs[(x + dx, y + dy)][1], steps + 2, visited))
		elif valid.get((x + dx, y + dy)):
			visited[(x + dx, y + dy)] = True
			Q.append((x + dx, y + dy, steps + 1, visited))

Q = deque([(start[0], start[1], 0, 0, {(start[0], start[1], 0):True})])
while Q:
	x, y, steps, level, visited = Q.popleft()
	for dx, dy in dirs:
		if (x + dx, y + dy) == end and level == 0:
			print(steps + 1)
			Q.clear()
			break
		if visited.get((x + dx, y + dy, level)):
			continue
		elif pairs.get((x + dx, y + dy)):
			if (x + dx, y + dy) in outer and level != 0:
				visited[(x + dx, y + dy, level)] = True
				visited[(pairs[(x + dx, y + dy)][0], pairs[(x + dx, y + dy)][1], level - 1)] = True
				Q.append((pairs[(x + dx, y + dy)][0], pairs[(x + dx, y + dy)][1], steps + 2, level - 1, visited))
			elif (x + dx, y + dy) in inner:
				visited[(x + dx, y + dy, level)] = True
				visited[(pairs[(x + dx, y + dy)][0], pairs[(x + dx, y + dy)][1], level + 1)] = True
				Q.append((pairs[(x + dx, y + dy)][0], pairs[(x + dx, y + dy)][1], steps + 2, level + 1, visited))
		elif valid.get((x + dx, y + dy)):
			visited[(x + dx, y + dy, level)] = True
			Q.append((x + dx, y + dy, steps + 1, level, visited))