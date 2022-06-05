from itertools import permutations

sits = {}
people = []
with open("13.txt") as f:
	for line in f:
		inp = line.strip().split(" ")
		if not inp[0] in people:
			people.append(inp[0])
		if not inp[0] in sits:
			sits[inp[0]] = {inp[10][:-1]: inp[2] == "gain" and int(inp[3]) or -int(inp[3])}
		else:
			sits[inp[0]][inp[10][:-1]] = inp[2] == "gain" and int(inp[3]) or -int(inp[3])

happy = []
ways = list(permutations(people))
for way in ways:
	count = 0
	for i in range(len(way)):
		count += sits[way[i]][way[(i-1) % len(way)]] + sits[way[i]][way[(i+1) % len(way)]]
	happy.append(count)
happy.sort()
print(happy[-1])

people.append("Me")
for k,v in sits.items():
	v["Me"] = 0
sits["Me"] = {k: 0 for k in sits.keys()}

happy = []
ways = list(permutations(people))
for way in ways:
	count = 0
	for i in range(len(way)):
		count += sits[way[i]][way[(i-1) % len(way)]] + sits[way[i]][way[(i+1) % len(way)]]
	happy.append(count)
happy.sort()
print(happy[-1])