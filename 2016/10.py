bots = {}
outs = {}
links = {}
with open("10.txt") as f:
	for line in f:
		inp = line.strip().split()
		if inp[0] == "value":
			if int(inp[5]) in bots:
				bots[int(inp[5])].append(int(inp[1]))
			else:
				bots[int(inp[5])] = [int(inp[1])]
		else:
			if not int(inp[1]) in links:
				links[int(inp[1])] = [inp[5] + inp[6], inp[10] + inp[11]]
			if inp[5] == "output":
				if not int(inp[6]) in outs:
					outs[int(inp[6])] = 0
			elif inp[5] == "bot":
				if not int(inp[6]) in bots:
					bots[int(inp[6])] = []
			if inp[10] == "output":
				if not int(inp[11]) in outs:
					outs[int(inp[11])] = 0
			elif inp[10] == "bot":
				if not int(inp[11]) in bots:
					bots[int(inp[11])] = []

while sum(len(bot) for bot in bots.values()) != 0:
	for bot, chips in bots.items():
		if len(chips) == 2:
			if 61 in chips and 17 in chips:
				print(bot)
			for ind, item in enumerate(links[bot]):
				if item[0:3] == "bot" and ind == 0:
					bots[int(item[3:])].append(min(chips))
				elif item[0:3] == "bot" and ind == 1:
					bots[int(item[3:])].append(max(chips))
				elif item[0:6] == "output" and ind == 0:
					outs[int(item[6:])] = min(chips)
				elif item[0:6] == "output" and ind == 1:
					outs[int(item[6:])] = max(chips)
			bots[bot] = []
print(outs[0]*outs[1]*outs[2])