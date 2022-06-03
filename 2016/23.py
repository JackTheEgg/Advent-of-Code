import copy

def runProg(prog, ind):
	while ind <= len(prog) - 1:
		if prog[ind][0] == "cpy":
			if prog[ind][1][-1].isnumeric() and not prog[ind][2][-1].isnumeric():
				regs[prog[ind][2]] = int(prog[ind][1])
				ind += 1
			elif not prog[ind][1][-1].isnumeric() and not prog[ind][2][-1].isnumeric():
				regs[prog[ind][2]] = regs[prog[ind][1]]
				ind += 1
			else:
				ind += 1
		elif prog[ind][0] == "inc":
			if not prog[ind][1][-1].isnumeric():
				regs[prog[ind][1]] += 1
				ind += 1
			else:
				ind += 1
		elif prog[ind][0] == "dec":
			if not prog[ind][1][-1].isnumeric():
				regs[prog[ind][1]] -= 1
				ind += 1
			else:
				ind += 1
		elif prog[ind][0] == "jnz":
			if prog[ind][1].isnumeric():
				if int(prog[ind][1]) != 0 and prog[ind][2][-1].isnumeric():
					ind += int(prog[ind][2])
				elif int(prog[ind][1]) != 0 and not prog[ind][2][-1].isnumeric():
					ind += regs[prog[ind][2]]
				else:
					ind += 1
			else:
				if regs[prog[ind][1]] != 0 and prog[ind][2][-1].isnumeric():
					ind += int(prog[ind][2])
				elif regs[prog[ind][1]] != 0 and not prog[ind][2][-1].isnumeric():
					ind += regs[prog[ind][2]]
				else:
					ind += 1
		elif prog[ind][0] == "tgl":
			if prog[ind][1][-1].isnumeric():
				newInd = ind + int(prog[ind][1])
			else:
				newInd = ind + regs[prog[ind][1]]
			if newInd < 0 or newInd >= len(prog):
				ind += 1
			else:
				if len(prog[newInd]) == 2:
					if prog[newInd][0] == "inc":
						prog[newInd][0] = "dec"
						ind += 1
					else:
						prog[newInd][0] = "inc"
						ind += 1
				elif len(prog[newInd]) == 3:
					if prog[newInd][0] == "jnz":
						prog[newInd][0] = "cpy"
						ind += 1
					else:
						prog[newInd][0] = "jnz"
						ind += 1

prog = []
with open("23.txt") as f:
	for line in f:
		row = line.strip().split(" ")
		prog.append(row)

regs = {"a":7, "b":0, "c":0, "d":0}	
runProg(copy.deepcopy(prog), 0)
print(regs["a"])

regs = {"a":12, "b":0, "c":0, "d":0}	
runProg(copy.deepcopy(prog), 0)
print(regs["a"])