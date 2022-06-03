links = {}
with open("12.txt") as f:
	for line in f:
		i = line.strip().split(" <-> ")
		links[int(i[0])] = list(map(int, i[1].split(", ")))

def getLinks(num):
	link = set(links[num])
	link.add(num)
	while True:
		check = len(link)
		newSet = set()
		for item in link:
			newSet = set.union(newSet, set(links[item]))
		link = set.union(newSet, link)
		if len(link) == check:
			return link

print(len(getLinks(0)))

groups = []
for num in links:
	if len(groups) == 0:
		groups.append(getLinks(num))
	else:
		found = False
		for group in groups:
			if num in group:
				found = True
				break
		if not found:
			groups.append(getLinks(num))
print(len(groups))