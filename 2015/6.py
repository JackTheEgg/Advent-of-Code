import re

lightsp1 = [[False for x in range(1000)] for y in range(1000)]
lightsp2 = [[0 for x in range(1000)] for y in range(1000)]
with open("6.txt") as f:
	for line in f:
		ranges = re.split("\D+", line.strip())
		ranges = list(map(int, ranges[1:]))
		instr = re.split("\W+", line.strip())
		if instr[0] == "toggle":
			for y in range(ranges[1], ranges[3] + 1):
				for x in range(ranges[0], ranges[2] + 1):
					if lightsp1[y][x] == True:
						lightsp1[y][x] = False
					elif lightsp1[y][x] == False:
						lightsp1[y][x] = True
					lightsp2[y][x] += 2
		elif instr[0] == "turn":
			if instr[1] == "on":
				for y in range(ranges[1], ranges[3] + 1):
					for x in range(ranges[0], ranges[2] + 1):
						lightsp1[y][x] = True
						lightsp2[y][x] += 1
			elif instr[1] == "off":
				for y in range(ranges[1], ranges[3] + 1):
					for x in range(ranges[0], ranges[2] + 1):
						lightsp1[y][x] = False
						if lightsp2[y][x] == 0:
							continue
						else:
							lightsp2[y][x] -= 1
print(sum(lightsp1[y][x] == True for y in range(1000) for x in range(1000)))
print(sum(lightsp2[y][x] for y in range(1000) for x in range(1000)))