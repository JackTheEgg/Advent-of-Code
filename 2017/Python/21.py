import math

def getAll(pat):
	pats = set()
	for i in range(4):
		pat = tuple(zip(*pat[::-1]))
		pats.add(pat)
	strs = set()
	for pat in pats:
		strs.add(tuple("".join(row) for row in pat))
	invs = set()
	for s in strs:
		invs.add(tuple(row[::-1] for row in s))
	union = strs.union(invs)
	return list(union)

def cut(item):
	crops = []
	size = len(item)
	if size % 2 == 0:
		for i in range(0, size, 2):
			s = item[i:i+2]
			for j in range(0, size, 2):
				crop = tuple(row[j:j+2] for row in s)
				crops.append(crop)
	else:
		for i in range(0, size, 3):
			s = item[i:i+3]
			for j in range(0, size, 3):
				crop = tuple(row[j:j+3] for row in s)
				crops.append(crop)
	return crops

def glue(pieces):
	joined = []
	L = len(pieces)
	side = round(math.sqrt(L))
	for i in range(0, L, side):
		s = pieces[i:i+side]
		for j in range(len(s[0])):
			row = ""
			for k in range(len(s)):
				row += s[k][j]
			joined.append(row)
	return tuple(joined)

pats = {}
with open("21.txt") as f:
	for line in f:
		inp, out = line.strip().split(" => ")
		out = out.split("/")
		inp = inp.split("/")
		newIn = []
		for row in inp:
			newIn.append(tuple(char for char in row))
		newIn = tuple(newIn)
		flips = getAll(newIn)
		for flip in flips:
			pats[flip] = tuple(out)

start = [(".#.", "..#", "###")]
for i in range(18):
	outs = []
	for item in start:
		outs.append(pats[item])
	outs = glue(outs)
	if i == 4:
		print(sum(row.count("#") for row in outs))
	start = cut(outs)
print(sum(row.count("#") for row in outs))