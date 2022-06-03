prog = []
with open("12.txt") as f:
	for line in f:
		row = line.strip().split(" ")
		prog.append(row)

regs = {"a":0, "b":0, "c":0, "d":0}

def runProg(prog, ind):
	while ind <= len(prog) - 1:
		if prog[ind][0] == "cpy":
			if prog[ind][1].isnumeric():
				regs[prog[ind][2]] = int(prog[ind][1])
			else:
				regs[prog[ind][2]] = regs[prog[ind][1]]
			ind += 1
		elif prog[ind][0] == "inc":
			regs[prog[ind][1]] += 1
			ind += 1
		elif prog[ind][0] == "dec":
			regs[prog[ind][1]] -= 1
			ind += 1
		elif prog[ind][0] == "jnz":
			if prog[ind][1].isnumeric():
				if int(prog[ind][1]) != 0:
					ind += int(prog[ind][2])
				else:
					ind += 1
			else:
				if int(regs[prog[ind][1]]) != 0:
					ind += int(prog[ind][2])
				else:
					ind += 1

ind = 0
runProg(prog, ind)
print(regs["a"])

regs = {"a":0, "b":0, "c":1, "d":0}
ind = 0
runProg(prog, ind)
print(regs["a"])