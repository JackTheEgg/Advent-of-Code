from itertools import combinations

jars = list(map(int, open("17.txt").read().splitlines()))

def getAllWays(lst):
	ways = []
	for i in range(1, len(lst)):
		ways += list(combinations(lst, i))
	return ways

ways = getAllWays(jars)
valids = []
count = 0
for way in ways:
	if sum(way) == 150:
		count += 1
		valids.append(way)
print(count)

total = sum(len(valid) == min(len(valid) for valid in valids) for valid in valids)
print(total)