inps = {}
wires = []
refs = {}
with open("7.txt") as f:
	for line in f:
		inp = line.strip().split(" -> ")
		chars = inp[0].split(" ")
		inps[inp[1]] = chars
		wires.append(inp[1])

def connect(refs, wires, inps):
	while len(refs) != len(wires):
		for wire, inp in inps.items():
			if len(inp) == 1:
				if inp[0].isnumeric() and not wire in refs:
					refs[wire] = int(inp[0])
				elif not wire in refs and inp[0] in refs:
					refs[wire] = refs[inp[0]]
			elif len(inp) == 2:
				if inp[1] in refs:
					refs[wire] = ~ refs[inp[1]]
			elif len(inp) == 3:
				if inp[1] == "AND":
					if inp[0].isnumeric() and inp[2] in refs:
						refs[wire] = int(inp[0]) & refs[inp[2]]
					elif inp[2].isnumeric() and inp[0] in refs:
						refs[wire] = refs[inp[0]] & int(inp[2])
					elif inp[0] in refs and inp[2] in refs:
						refs[wire] = refs[inp[0]] & refs[inp[2]]
				elif inp[1] == "OR":
					if inp[0].isnumeric() and inp[2] in refs:
						refs[wire] = int(inp[0]) | refs[inp[2]]
					elif inp[2].isnumeric() and inp[0] in refs:
						refs[wire] = refs[inp[0]] | int(inp[2])
					elif inp[0] in refs and inp[2] in refs:
						refs[wire] = refs[inp[0]] | refs[inp[2]]
				elif inp[1] == "RSHIFT" and inp[0] in refs:
					refs[wire] = refs[inp[0]] >> int(inp[2])
				elif inp[1] == "LSHIFT" and inp[0] in refs:
					refs[wire] = refs[inp[0]] << int(inp[2])

connect(refs, wires, inps)
print(refs["a"])

override = refs["a"]
refs = {}
inps["b"][0] = str(override)
connect(refs, wires, inps)
print(refs["a"])