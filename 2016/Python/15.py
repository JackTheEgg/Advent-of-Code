import re

discs = []
with open("15.txt") as f:
	for line in f:
		disc = list(map(int, re.findall("-?[0-9]+", line.strip())))
		discs.append(disc)

t = 0
while True:
	count = 0
	for disc in discs:
		if disc[0] == 1:
			check = (disc[3] + disc[0] + t) % disc[1]
			count += 1
		elif check == (disc[3] + disc[0] + t) % disc[1]:
			count += 1
	if count == len(discs):
		print(t)
		break
	t += 1

discs.append([7, 11, 0, 0])
t = 0
while True:
	count = 0
	for disc in discs:
		if disc[0] == 1:
			check = (disc[3] + disc[0] + t) % disc[1]
			count += 1
		elif check == (disc[3] + disc[0] + t) % disc[1]:
			count += 1
	if count == len(discs):
		print(t)
		break
	t += 1