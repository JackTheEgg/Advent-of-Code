regs = {}
with open("8.txt") as f:
	for line in f:
		i = line.strip().split()
		if not i[0] in regs:
			regs[i[0]] = 0
		if not i[4] in regs:
			regs[i[4]] = 0

vals = []
with open("8.txt") as f:
	for line in f:
		i = line.strip().split()
		if i[5] == "<" and (regs[i[4]] < int(i[6])):
			if i[1] == "inc":
				regs[i[0]] += int(i[2])
				vals.append(regs[i[0]])
			else:
				regs[i[0]] -= int(i[2])
				vals.append(regs[i[0]])
		elif i[5] == ">" and (regs[i[4]] > int(i[6])):
			if i[1] == "inc":
				regs[i[0]] += int(i[2])
				vals.append(regs[i[0]])
			else:
				regs[i[0]] -= int(i[2])
				vals.append(regs[i[0]])
		elif i[5] == "!=" and (regs[i[4]] != int(i[6])):
			if i[1] == "inc":
				regs[i[0]] += int(i[2])
				vals.append(regs[i[0]])
			else:
				regs[i[0]] -= int(i[2])
				vals.append(regs[i[0]])
		elif i[5] == ">=" and (regs[i[4]] >= int(i[6])):
			if i[1] == "inc":
				regs[i[0]] += int(i[2])
				vals.append(regs[i[0]])
			else:
				regs[i[0]] -= int(i[2])
				vals.append(regs[i[0]])
		elif i[5] == "<=" and (regs[i[4]] <= int(i[6])):
			if i[1] == "inc":
				regs[i[0]] += int(i[2])
				vals.append(regs[i[0]])
			else:
				regs[i[0]] -= int(i[2])
				vals.append(regs[i[0]])
		elif i[5] == "==" and (regs[i[4]] == int(i[6])):
			if i[1] == "inc":
				regs[i[0]] += int(i[2])
				vals.append(regs[i[0]])
			else:
				regs[i[0]] -= int(i[2])
				vals.append(regs[i[0]])
print(max(regs.values()))
print(max(vals))