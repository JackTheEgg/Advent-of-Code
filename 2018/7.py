from string import ascii_uppercase
from copy import deepcopy

reqs = {}
letters = set()
with open("7.txt") as f:
	for line in f:
		inp = line.strip().split()
		letters.add(inp[1])
		letters.add(inp[-3])
		if not inp[-3] in reqs:
			reqs[inp[-3]] = [inp[1]]
		else:
			reqs[inp[-3]].append(inp[1])
	for letter in letters:
		if not letter in reqs:
			reqs[letter] = []
reqs2 = deepcopy(reqs)

s = ""
while len(reqs) > 0:
	pos = []
	for letter, req in reqs.items():
		if len(req) == 0:
			pos.append(letter)
	pos.sort()
	s += pos[0]
	for letter, req in reqs.items():
		if pos[0] in req:
			reqs[letter].remove(pos[0])
	del reqs[pos[0]]
print(s)

U = ascii_uppercase
times = {U[i]: i + 61 for i in range(len(U))}
time = 0
workers = {i:"" for i in range(5)}
innerTimes = {}

while len(reqs2) > 0:
	pos = []
	for letter, req in reqs2.items():
		if len(req) == 0 and not letter in workers.values():
			pos.append(letter)
	pos.sort()
	if len(pos) > 0:
		i = 0
		for w, letter in workers.items():
			if letter == "":
				workers[w] = pos[i]
				i += 1
				if i == len(pos): break
	place = []
	for char in workers.values():
		if char != "" and not char in innerTimes:
			innerTimes[char] = 1
		elif char in innerTimes:
			innerTimes[char] += 1
			if innerTimes[char] == times[char]:
				place.append(char)
	for char in place:
		del innerTimes[char]
		for letter, req in reqs2.items():
			if char in req:
				reqs2[letter].remove(char)
		del reqs2[char]
		for w, letter in workers.items():
			if letter == char:
				workers[w] = ""
	time += 1
print(time)