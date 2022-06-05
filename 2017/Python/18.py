def runProg(prog, regs, i, inpInd, ver, part2 = False):
	movCount = 0
	while i <= len(prog) - 1:
		if prog[i][0] == "snd":
			if not part2:
				if prog[i][1] in regs:
					sounds.append(regs[prog[i][1]])
				else:
					sounds.append(int(prog[i][1]))
			else:
				if ver == 0:
					if prog[i][1] in regs:
						vals1.append(regs[prog[i][1]])
					else:
						vals1.append(int(prog[i][1]))
				else:
					if prog[i][1] in regs:
						vals0.append(regs[prog[i][1]])
					else:
						vals0.append(int(prog[i][1]))								
			i += 1
			movCount += 1
		elif prog[i][0] == "set":
			if prog[i][2] in regs:
				regs[prog[i][1]] = regs[prog[i][2]]
			else:
				regs[prog[i][1]] = int(prog[i][2])
			i += 1
			movCount += 1
		elif prog[i][0] == "add":
			if prog[i][2] in regs:
				regs[prog[i][1]] += regs[prog[i][2]]
			else:
				regs[prog[i][1]] += int(prog[i][2])
			i += 1
			movCount += 1
		elif prog[i][0] == "mul":
			if prog[i][2] in regs:
				regs[prog[i][1]] *= regs[prog[i][2]]
			else:
				regs[prog[i][1]] *= int(prog[i][2])
			i += 1	
			movCount += 1
		elif prog[i][0] == "mod":
			if prog[i][2] in regs:
				regs[prog[i][1]] %= regs[prog[i][2]]
			else:
				regs[prog[i][1]] %= int(prog[i][2])
			i += 1
			movCount += 1
		elif prog[i][0] == "rcv":
			if not part2:
				if prog[i][1] in regs:
					if regs[prog[i][1]] != 0:
						return sounds[-1]
				elif int(prog[i][1]) != 0:
					return sounds[-1]
				i += 1
			else:
				if ver == 1:
					if inpInd <= len(vals1) - 1:
						regs[prog[i][1]] = vals1[inpInd]
						inpInd += 1
						i += 1
						movCount += 1
					else:
						if movCount == 0:
							return regs, i, inpInd, True
						else:
							return regs, i, inpInd, False
				else:
					if inpInd <= len(vals0) - 1:
						regs[prog[i][1]] = vals0[inpInd]
						inpInd += 1
						i += 1
						movCount += 1
					else:
						if movCount == 0:
							return regs, i, inpInd, True
						else:
							return regs, i, inpInd, False
		elif prog[i][0] == "jgz":
			if prog[i][1] in regs:
				if regs[prog[i][1]] > 0:
					if prog[i][2] in regs:
						i += regs[prog[i][2]]
					else:
						i += int(prog[i][2])
				else:
					i += 1
			elif int(prog[i][1]) > 0:
				if prog[i][2] in regs:
					i += regs[prog[i][2]]
				else:
					i += int(prog[i][2])
			else:
				i += 1
			movCount += 1
	return regs, i, inpInd, True

sounds = []
prog = []
regs = {}
with open("18.txt") as f:
	for line in f:
		row = line.strip().split()
		if len(row) == 2:
			if row[1].islower() and not row[1] in regs:
				regs[row[1]] = 0
		else:
			if row[1].islower() and not row[1] in regs:
				regs[row[1]] = 0
			if row[2].islower() and not row[2] in regs:
				regs[row[2]] = 0
		prog.append(row)

print(runProg(prog, regs, 0, "", ""))  # runProg(prog, regs, i, inpInd, ver, part2 = False)

regs0 = {x:0 for x in regs.keys()}
regs1 = {x:0 for x in regs.keys() if x != "p"}
regs1["p"] = 1
vals0, vals1 = [], []
ver0, ver1 = 0, 1
i0, i1 = 0, 0
inpInd0, inpInd1 = 0, 0

while True:
	regs0, i0, inpInd0, isBlocked0 = runProg(prog, regs0, i0, inpInd0, 0, True)
	regs1, i1, inpInd1, isBlocked1 = runProg(prog, regs1, i1, inpInd1, 1, True)
	if isBlocked1 and isBlocked0:
		break
print(len(vals0))