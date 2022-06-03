from parse import *

def parseIn(boost):
	units = {}
	inp = open("24.txt").readlines()
	for i, line in enumerate(inp):
		if "units" in line:
			if "immune" in line and "weak" in line:
				a = parse("{U:d} units each with {HP:d} hit points (immune to {I}; weak to {W}) with an attack that does {D:d} {dType} damage at initiative {Init:d}", line.strip())
				a = a.named
				if i < len(inp) // 2:
					a["Type"] = "IS"
					a["TD"] = 0
					units[i] = a
				else:
					a["Type"] = "I"
					a["TD"] = 0
					units[i] = a
			elif "immune" in line:
				a = parse("{U:d} units each with {HP:d} hit points (immune to {I}) with an attack that does {D:d} {dType} damage at initiative {Init:d}", line.strip())
				a = a.named
				a["W"] = ""
				if i < len(inp) // 2:
					a["Type"] = "IS"
					a["TD"] = 0
					units[i] = a
				else:
					a["Type"] = "I"
					a["TD"] = 0
					units[i] = a
			elif "weak" in line:
				a = parse("{U:d} units each with {HP:d} hit points (weak to {W}) with an attack that does {D:d} {dType} damage at initiative {Init:d}", line.strip())
				a = a.named
				a["I"] = ""
				if i < len(inp) // 2:
					a["Type"] = "IS"
					a["TD"] = 0
					units[i] = a
				else:
					a["Type"] = "I"
					a["TD"] = 0
					units[i] = a
			else:
				a = parse("{U:d} units each with {HP:d} hit points with an attack that does {D:d} {dType} damage at initiative {Init:d}", line.strip())
				a = a.named
				a["W"] = ""
				a["I"] = ""
				if i < len(inp) // 2:
					a["Type"] = "IS"
					a["TD"] = 0
					units[i] = a
				else:
					a["Type"] = "I"
					a["TD"] = 0
					units[i] = a
	for k, v in units.items():
		if v["Type"] == "IS":
			units[k]["D"] += boost
			units[k]["EP"] = units[k]["D"] * units[k]["U"]
		else:
			units[k]["EP"] = units[k]["D"] * units[k]["U"]
	return units

def turn(units):
	lostUnits = False
	picked = {}
	units = {k:v for k, v in sorted(units.items(), key = lambda x: (x[1]["EP"], x[1]["Init"]), reverse = True)}
	for num, info in units.items():
		others = {k: v for k, v in units.items() if v != info}
		potential = {}
		for k, v in others.items():
			if info["Type"] == "IS":
				if v["Type"] == "I" and not k in picked.values():
					if info["dType"] not in v["W"] and info["dType"] not in v["I"]:
						others[k]["TD"] = info["EP"]
						potential[k] = others[k]
					elif info["dType"] in v["W"]:
						others[k]["TD"] = info["EP"] * 2
						potential[k] = others[k]
					elif info["dType"] in v["I"]:
						others[k]["TD"] = 0
						potential[k] = others[k]
			else:
				if v["Type"] == "IS" and not k in picked.values():
					if info["dType"] not in v["W"] and info["dType"] not in v["I"]:
						others[k]["TD"] = info["EP"]
						potential[k] = others[k]
					elif info["dType"] in v["W"]:
						others[k]["TD"] = info["EP"] * 2
						potential[k] = others[k]
					elif info["dType"] in v["I"]:
						others[k]["TD"] = 0
						potential[k] = others[k]
		if len(potential) != 0:
			potential = {k: v for k, v in sorted(potential.items(), key = lambda x: (x[1]["TD"], x[1]["EP"], x[1]["Init"]), reverse = True)}
			for k, v in potential.items():
				if v["TD"] != 0:
					picked[num] = k
					units[k]["TD"] = v["TD"]
					break
	sortedI = sorted(list(k["Init"] for k in units.values()), reverse = True)
	spicked = {}
	for num in sortedI:
		for k in picked:
			if units[k]["Init"] == num:
				spicked[k] = picked[k]
				break
	killed = []
	for a, d in spicked.items():
		if not d in killed:
			start = units[d]["U"]
			units[d]["U"] -= (units[d]["TD"] // units[d]["HP"])
			if units[d]["U"] != start: 
				lostUnits = True
			if units[d]["U"] <= 0:
				killed.append(d)
				if d in spicked.keys():
					units[spicked[d]]["TD"] = 0
			else:
				if d in spicked.keys():
					units[spicked[d]]["TD"] *= (units[d]["U"] / start)
		elif d in killed:
			if d in spicked.keys():
				units[spicked[d]]["TD"] = 0
	for n in killed:
		del units[n]
	for k in units:
		units[k]["TD"] = 0
		units[k]["EP"] = units[k]["D"] * units[k]["U"]
	if not lostUnits:
		return units, True
	else:
		return units, False

for n in range(1000000):
	units = parseIn(n)
	endless = False
	while "I" in list(k["Type"] for k in units.values()) and "IS" in list(k["Type"] for k in units.values()) and not endless:
		units, endless = turn(units)
	if n == 0:
		print(round(sum([k["U"] for k in units.values()])))
	else:
		if "IS" in list(k["Type"] for k in units.values()) and not "I" in list(k["Type"] for k in units.values()):
			print(round(sum([k["U"] for k in units.values()])))
			break