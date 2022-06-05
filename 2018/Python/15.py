from copy import deepcopy

units = {}
valid = set()
count = 1
with open("15.txt") as f:
	for y, line in enumerate(f):
		for x, char in enumerate(line.rstrip("\n")):
			if char == ".":
				valid.add((x,y))
			elif char == "G":
				units[count] = {"P":(x, y), "HP":200, "Type":"G"}
				count += 1
				valid.add((x,y))
			elif char == "E":
				units[count] = {"P":(x, y), "HP":200, "Type":"E"}
				count += 1
				valid.add((x,y))
maxElves = sum(k["Type"] == "E" for k in units.values())

dirs = [(0,-1), (-1,0), (1,0), (0,1)]
movs = {(1,0):"R", (-1,0):"L", (0,1):"D", (0,-1):"U"}
step = {v:k for k,v in movs.items()}

def isInRange(pos, Type, goblins, elves):
	adj = list((pos[0] + d[0], pos[1] + d[1]) for d in dirs)
	if Type == "G":
		for coord in adj:
			if coord in elves:
				return True
	else:
		for coord in adj:
			if coord in goblins:
				return True
	return False

def getAdj(Type, goblins, elves, valid):
	if Type == "G":
		return list((e[0] + d[0], e[1] + d[1]) for e in elves for d in dirs if (e[0] + d[0], e[1] + d[1]) in valid and (e[0] + d[0], e[1] + d[1]) not in elves and (e[0] + d[0], e[1] + d[1]) not in goblins)
	else:
		return list((e[0] + d[0], e[1] + d[1]) for e in goblins for d in dirs if (e[0] + d[0], e[1] + d[1]) in valid and (e[0] + d[0], e[1] + d[1]) not in elves and (e[0] + d[0], e[1] + d[1]) not in goblins)

def attack(pos, Type, units):
	adj = list((pos[0] + d[0], pos[1] + d[1]) for d in dirs)
	inRange = {k:v for k, v in units.items() if v["P"] in adj and v["Type"] != Type and v["HP"] > 0}
	inRange = {k:v for k, v in sorted(inRange.items(), key = lambda x: (x[1]["HP"], x[1]["P"][1], x[1]["P"][0]))}
	return list(inRange.keys())[0]

def getPaths(paths, visited, pos, adj, goblins, elves):
	newPaths, goal, willGo = set(), set(), set()
	for p in paths:
		for d in dirs:
			if (p[0][0] + d[0], p[0][1] + d[1]) in adj:
				route = p[1]
				if route == "":
					route = movs[d]
					goal.add((p[0][0] + d[0], p[0][1] + d[1], pos[0] + step[route][0], pos[1] + step[route][1]))
				else:
					goal.add((p[0][0] + d[0], p[0][1] + d[1], pos[0] + step[route][0], pos[1] + step[route][1]))
			elif (p[0][0] + d[0], p[0][1] + d[1]) in valid and (p[0][0] + d[0], p[0][1] + d[1]) not in visited and (p[0][0] + d[0], p[0][1] + d[1]) not in elves and (p[0][0] + d[0], p[0][1] + d[1]) not in goblins:
				route = p[1]
				if route == "":
					route = movs[d]
					willGo.add((p[0][0] + d[0], p[0][1] + d[1]))
					newPaths.add(((p[0][0] + d[0], p[0][1] + d[1]), route))
				else:
					willGo.add((p[0][0] + d[0], p[0][1] + d[1]))
					newPaths.add(((p[0][0] + d[0], p[0][1] + d[1]), route))	
	if len(goal) > 0:
		goal = sorted(list(goal), key = lambda x: (x[1], x[0], x[3], x[2]))
		return (goal[0][2], goal[0][3]), visited, True
	visited.update(willGo)
	return newPaths, visited, False

def turn(units, Round, boost, part2 = False):
	units = {k:v for k, v in sorted(units.items(), key = lambda x: (x[1]["P"][1], x[1]["P"][0]))}
	for u, info in units.items():
		surv = list(k["Type"] for k in units.values() if k["HP"] > 0)
		if part2 and surv.count("E") < maxElves:
			return units, True, Round, False
		if not "G" in surv:
			return units, True, Round, True
		elif not "E" in surv: 
			return units, True, Round, False
		goblins = list(k["P"] for k in units.values() if (k["Type"] == "G" and k["HP"] > 0))
		elves = list(k["P"] for k in units.values() if (k["Type"] == "E" and k["HP"] > 0))
		if info["HP"] > 0:
			if isInRange(info["P"], info["Type"], goblins, elves):
				damaged = attack(info["P"], info["Type"], units)
				if units[damaged]["Type"] == "G":
					units[damaged]["HP"] -= (3 + boost)
				else:
					units[damaged]["HP"] -= 3
			else:
				adj = getAdj(info["Type"], goblins, elves, valid)
				if len(adj) > 0:
					visited, paths = set(), set()
					visited.add(info["P"])
					paths.add((info["P"], ""))
					found = False
					while not found and len(paths) > 0:
						paths, visited, found = getPaths(paths, visited, info["P"], adj, goblins, elves)
					if found:
						units[u]["P"] = paths
					if isInRange(info["P"], info["Type"], goblins, elves):
						damaged = attack(info["P"], info["Type"], units)
						if units[damaged]["Type"] == "G":
							units[damaged]["HP"] -= (3 + boost)
						else:
							units[damaged]["HP"] -= 3
	return units, False, Round + 1, False

for i in range(100000):
	test = deepcopy(units)
	Round = 0
	ended = False
	if i == 0:
		while not ended:
			test, ended, Round, elvesWon = turn(test, Round, i)
		print(Round * sum(k["HP"] for k in test.values() if k["HP"] > 0))
	else:
		while not ended:
			test, ended, Round, elvesWon = turn(test, Round, i, True)
		if elvesWon:
			print(Round * sum(k["HP"] for k in test.values() if k["HP"] > 0))
			break	