from itertools import permutations

cities = []
dists = {}
with open("9.txt") as f:
	for line in f:
		inp = line.strip().split(" ")
		if not inp[0] in cities: 
			cities.append(inp[0])
		if not inp[2] in cities: 
			cities.append(inp[2])
		if not inp[0] in dists:
			dists[inp[0]] = {inp[2]: int(inp[4])}
		else:
			if not inp[2] in dists[inp[0]]:
				dists[inp[0]][inp[2]] = int(inp[4])
		if not inp[2] in dists:
			dists[inp[2]] = {inp[0]: int(inp[4])}
		else:
			if not inp[0] in dists[inp[2]]:
				dists[inp[2]][inp[0]] = int(inp[4])

routes = list(permutations(cities))
lengths = []
for route in routes:
	count = 0
	for i in range(len(route) - 1):
		count += dists[route[i]][route[i+1]]
	lengths.append(count)
lengths.sort()
print(lengths[0])
print(lengths[-1])