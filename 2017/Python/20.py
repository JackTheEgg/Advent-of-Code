import re
from copy import deepcopy

particlesp1 = {}
with open("20.txt") as f:
	for ind, line in enumerate(f):
		nums = list(map(int, re.findall("-?[0-9]+", line.strip())))
		particlesp1[ind] = {"p": nums[:3], "v": nums[3:6], "a": nums[6:]}
particlesp2 = deepcopy(particlesp1)

for n in range(1000):
	for k, v in particlesp1.items():
		for i in range(len(v["v"])):
			v["v"][i] += v["a"][i]
		for i in range(len(v["v"])):
			v["p"][i] += v["v"][i]

for k, v in particlesp1.items():
	if sum(map(abs, v["p"])) == min(sum(map(abs, particlesp1[i]["p"])) for i in particlesp1.keys()):
		print(k)
		break

for n in range(1000):
	pos = []
	for k, v in particlesp2.items():
		for i in range(len(v["v"])):
			v["v"][i] += v["a"][i]
		for i in range(len(v["v"])):
			v["p"][i] += v["v"][i]
		pos.append(tuple(v["p"]))
	if not len(pos) == len(set(pos)):
		delete = []
		for item in set(pos):
			if pos.count(item) > 1:
				delete.append(list(item))
		keys = []
		for k, v in particlesp2.items():
			if v["p"] in delete:
				keys.append(k)
		for k in keys:
			del particlesp2[k]
print(len(particlesp2))