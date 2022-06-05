aunts = {}
with open("16.txt") as f:
	for line in f:
		inp = line.strip().split(" ")
		info = {inp[2:][i][:-1]: int(inp[2:][i+1][:-1]) for i in range(0, len(inp[2:]) - 2, 2)}
		info[inp[2:][4][:-1]] = int(inp[2:][5])
		aunts[int(inp[1][:-1])] = info

facts = {
	"children": 3,
	"cats": 7,
	"samoyeds": 2,
	"pomeranians": 3,
	"akitas": 0,
	"vizslas": 0,
	"goldfish": 5,
	"trees": 3,
	"cars": 2,
	"perfumes": 1,
}

def scan1(dct, facts):
	for item in dct.keys():
		if not dct[item] == facts[item]:
			return False
	return True

def scan2(dct, facts):
	for item in dct.keys():
		if item == "trees" or item == "cats":
			if not dct[item] > facts[item]:
				return False
		elif item == "pomeranians" or item == "goldfish":
			if not dct[item] < facts[item]:
				return False
		else:
			if not dct[item] == facts[item]:
				return False
	return True

for aunt, info in aunts.items():
	if scan1(info, facts):
		print(aunt)
		break

for aunt, info in aunts.items():
	if scan2(info, facts):
		print(aunt)
		break