points = []
with open("25.txt") as f:
	for line in f:
		coords = tuple(map(int, line.strip().split(",")))
		points.append(coords)

count = 1
consts = {}
for point in points:
	if not count in consts:
		consts[count] = [point]
	else:
		noBelong = True
		for k, v in consts.items():
			for item in v:
				if sum(map(abs, [item[i] - point[i] for i in range(4)])) <= 3:
					consts[k].append(point)
					noBelong = False
					break
		if noBelong:
			count += 1
			consts[count] = [point]

def groupConsts(consts):
	newConsts = {}
	i = 1
	c = list(consts.values())
	for n in range(len(c)):
		const = c[n]
		others = [x for j,x in enumerate(c) if j != n]
		grouped = set()
		for val in const:
			grouped.add(val)
		for other in others:
			if len(list(const) + list(other)) != len(set(list(const) + list(other))):
				for val in other:
					grouped.add(val)
		if not grouped in newConsts.values():
			newConsts[i] = grouped
			i += 1
	return newConsts

while True:
	check = len(consts)
	consts = groupConsts(consts)
	if len(consts) == check:
		break
print(len(consts))