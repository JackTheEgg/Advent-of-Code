def step(o, t, l, w, h):
	o2, t2, l2 = [], [], []
	for y in range(h):
		for x in range(w):
			adj = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if (x + i, y + j) != (x,y)]
			if (x,y) in o:
				if sum(pair in t for pair in adj) >= 3:
					t2.append((x,y))
				else:
					o2.append((x,y))
			elif (x,y) in t:
				if sum(pair in l for pair in adj) >= 3:
					l2.append((x,y))
				else:
					t2.append((x,y))
			elif (x,y) in l:
				if (sum(pair in l for pair in adj) >= 1) and (sum(pair in t for pair in adj) >= 1):
					l2.append((x,y))
				else:
					o2.append((x,y))
	return o2, t2, l2

o, t, l = [], [], []
with open("18.txt") as file:
	for y, line in enumerate(file):
		w = len(line.strip())
		for x, char in enumerate(line.strip()):
			if char == ".":
				o.append((x,y))
			elif char == "|":
				t.append((x,y))
			elif char == "#":
				l.append((x,y))
		h = y + 1

part1 = 10
part2 = 1000000000
regs = [(o, t, l)]
while True:
	o, t, l = step(o, t, l, w, h)
	if (o, t, l) in regs:
		print(len(regs[part1][1]) * len(regs[part1][2]))
		part2 -= len(regs)
		regs = regs[regs.index((o, t, l)):]
		break
	else:
		regs.append((o, t, l))
print(len(regs[part2 % len(regs)][1]) * len(regs[part2 % len(regs)][2]))