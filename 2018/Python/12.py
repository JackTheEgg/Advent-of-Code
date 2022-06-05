rules = {}
pots = {}
with open("12.txt") as f:
	for y, line in enumerate(f):
		if y == 0:
			inp = line.strip().split()
			for i, char in enumerate(inp[2]):
				pots[i] = char
		elif y >= 2:
			start, end = line.strip().split(" => ")
			rules[start] = end

def step(pots):
	newPots = {}
	for n in range(min(pots.keys()) - 5, max(pots.keys()) + 5):
		row = ""
		for k in range(n-2, n+3):
			if not k in pots:
				row += "."
			else:
				row += pots[k]
		newPots[n] = rules[row]
	return newPots

part1 = 20
part2 = 50000000000
scores = {}
for n in range(1000):
	check = None
	scores[n] = sum([k for k, v in pots.items() if v == "#"])
	if len(scores) >= 2:
		check = scores[n] - scores[n-1]
	pots = step(pots)
	if (sum([k for k, v in pots.items() if v == "#"]) - scores[n]) == check:
		print(scores[20])
		part2 -= n + 1
		score = sum([k for k, v in pots.items() if v == "#"])
		break
print(score + check * part2)