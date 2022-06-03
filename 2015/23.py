prog = []
with open("23.txt") as f:
	for line in f:
		inp = line.strip().split()
		if inp[0] == "jio":
			inp[1] = inp[1][:-1]
			inp[2] = int(inp[2])
		elif inp[0] == "jie":
			inp[1] = inp[1][:-1]
			inp[2] = int(inp[2])
		elif inp[0] == "jmp":
			inp[1] = int(inp[1])
		prog.append(inp)

regs = {"a": 0, "b": 0}

def runProg(prog, ind, regs):
	while ind <= len(prog) - 1:
		if prog[ind][0] == "hlf":
			regs[prog[ind][1]] /= 2
			ind += 1
		elif prog[ind][0] == "tpl":
			regs[prog[ind][1]] *= 3
			ind += 1
		elif prog[ind][0] == "inc":
			regs[prog[ind][1]] += 1
			ind += 1
		elif prog[ind][0] == "jmp":
			ind += prog[ind][1]
		elif prog[ind][0] == "jie":
			if regs[prog[ind][1]] % 2 == 0:
				ind += prog[ind][2]
			else:
				ind += 1
		elif prog[ind][0] == "jio":
			if regs[prog[ind][1]] == 1:
				ind += prog[ind][2]
			else:
				ind += 1
	return regs
regs1 = runProg(prog, 0, regs.copy())
print(regs1["b"])

regs2 = regs.copy()
regs2["a"] = 1
regs2 = runProg(prog, 0, regs2)
print(regs2["b"])