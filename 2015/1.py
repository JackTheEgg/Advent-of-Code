floor = 0
with open("1.txt") as f:
	for line in f:
		for char in line.strip():
			if char == "(":
				floor += 1
			elif char == ")":
				floor -= 1
print(floor)

floor = 0
with open("1.txt") as f:
	for line in f:
		for ind, char in enumerate(line.strip()):
			if char == "(":
				floor += 1
			elif char == ")":
				floor -= 1
			if floor == -1:
				print(ind + 1)
				break	