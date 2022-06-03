from copy import deepcopy

intrs, Bturns, Fturns = [], [], []
carts = {}
turnR = {"U":"R", "R":"D", "D":"L", "L":"U"}
turnL = {v:k for k, v in turnR.items()}
nextTurn = {"L":"F", "F":"R", "R":"L"}
dirs = {"U":(0,-1), "D":(0,1), "L":(-1,0), "R":(1,0)}
count = 1
with open("13.txt") as f:
	for y, line in enumerate(f):
		for x, char in enumerate(line.rstrip("\n")):
			if char == "+":
				intrs.append((x,y))
			elif char == "\\":
				Bturns.append((x,y))
			elif char == "/":
				Fturns.append((x,y))
			elif char == ">":
				carts[count] = {"p":(x,y), "f":"R", "nTurn":"L"}
				count += 1 
			elif char == "v":
				carts[count] = {"p":(x,y), "f":"D", "nTurn":"L"}
				count += 1
			elif char == "^":
				carts[count] = {"p":(x,y), "f":"U", "nTurn":"L"}
				count += 1
			elif char == "<":
				carts[count] = {"p":(x,y), "f":"L", "nTurn":"L"}
				count += 1
carts2 = deepcopy(carts)

def step(carts, part2 = False):
	crashed = set()
	carts = {k: v for k, v in sorted(carts.items(), key = lambda x: x[1]["p"][1])}
	for num, info in carts.items():
		if num in crashed: continue
		info["p"] = (info["p"][0] + dirs[info["f"]][0], info["p"][1] + dirs[info["f"]][1])
		pos = list(i["p"] for i in carts.values())
		if len(set(pos)) != len(pos):
			if part2:
				for pair in pos:
					if pos.count(pair) > 1:
						for k, v in carts.items():
							if v["p"] == pair:
								crashed.add(k)
			else:
				for pair in pos:
					if pos.count(pair) > 1:
						return pair, True, crashed
		if info["p"] in Bturns:
			if info["f"] == "U" or info["f"] == "D":
				info["f"] = turnL[info["f"]]
			else:
				info["f"] = turnR[info["f"]]
		elif info["p"] in Fturns:
			if info["f"] == "U" or info["f"] == "D":
				info["f"] = turnR[info["f"]]
			else:
				info["f"] = turnL[info["f"]]			
		elif info["p"] in intrs:
			if info["nTurn"] == "L":
				info["f"] = turnL[info["f"]]
				info["nTurn"] = nextTurn[info["nTurn"]]
			elif info["nTurn"] == "R":
				info["f"] = turnR[info["f"]]
				info["nTurn"] = nextTurn[info["nTurn"]]
			elif info["nTurn"] == "F":
				info["nTurn"] = nextTurn[info["nTurn"]]
	if len(crashed) > 0:
		return carts, True, crashed
	else:
		return carts, False, crashed

crash = False
while not crash:
	carts, crash, crashed = step(carts)
print(carts)

while len(carts2) > 1:
	crash = False
	while not crash:
		carts2, crash, crashed = step(carts2, True)
	for cart in crashed:
		del carts2[cart]
for k, v in carts2.items():
	print(v["p"])					