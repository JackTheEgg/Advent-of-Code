from itertools import combinations
import math

packs = list(map(int, open("24.txt").read().splitlines()))
goalp1 = sum(packs) / 3
goalp2 = sum(packs) / 4
def getAllWays(lst, n1, n2):
	ways = []
	for i in range(n1, n2+1):
		ways += list(combinations(lst, i))
	return ways

combs = getAllWays(packs, 0, 6)
p1Packs = []
p2Packs = []
for comb in combs:
	if sum(comb) == goalp1:
		p1Packs.append(comb)
	elif sum(comb) == goalp2:
		p2Packs.append(comb)
smallestp1 = []
smallestp2 = []
for pack in p1Packs:
	if len(pack) == min(len(pack) for pack in p1Packs):
		smallestp1.append(pack)
for pack in p2Packs:
	if len(pack) == min(len(pack) for pack in p2Packs):
		smallestp2.append(pack)
print(min(math.prod(pack) for pack in smallestp1))
print(min(math.prod(pack) for pack in smallestp2))