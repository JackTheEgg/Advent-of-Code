import re

def runProg(regs, opc, inp1, inp2, out):
	if opc == "addr" or opc == opcodes["addr"]:
		regs[out] = regs[inp1] + regs[inp2]
		return regs
	elif opc == "addi" or opc == opcodes["addi"]:
		regs[out] = regs[inp1] + inp2
		return regs
	elif opc == "mulr" or opc == opcodes["mulr"]:
		regs[out] = regs[inp1] * regs[inp2]
		return regs
	elif opc == "muli" or opc == opcodes["muli"]:
		regs[out] = regs[inp1] * inp2
		return regs
	elif opc == "banr" or opc == opcodes["banr"]:
		regs[out] = regs[inp1] & regs[inp2]
		return regs
	elif opc == "bani" or opc == opcodes["bani"]:
		regs[out] = regs[inp1] & inp2
		return regs
	elif opc == "borr" or opc == opcodes["borr"]:
		regs[out] = regs[inp1] | regs[inp2]
		return regs
	elif opc == "bori" or opc == opcodes["bori"]:
		regs[out] = regs[inp1] | inp2
		return regs
	elif opc == "setr" or opc == opcodes["setr"]:
		regs[out] = regs[inp1]
		return regs
	elif opc == "seti" or opc == opcodes["seti"]:
		regs[out] = inp1
		return regs
	elif opc == "gtir" or opc == opcodes["gtir"]:
		if inp1 > regs[inp2]:
			regs[out] = 1
		else:
			regs[out] = 0
		return regs
	elif opc == "gtri" or opc == opcodes["gtri"]:
		if regs[inp1] > inp2:
			regs[out] = 1
		else:
			regs[out] = 0
		return regs
	elif opc == "gtrr" or opc == opcodes["gtrr"]:
		if regs[inp1] > regs[inp2]:
			regs[out] = 1
		else:
			regs[out] = 0
		return regs
	elif opc == "eqir" or opc == opcodes["eqir"]:
		if inp1 == regs[inp2]:
			regs[out] = 1
		else:
			regs[out] = 0
		return regs
	elif opc == "eqri" or opc == opcodes["eqri"]:
		if regs[inp1] == inp2:
			regs[out] = 1
		else:
			regs[out] = 0
		return regs
	elif opc == "eqrr" or opc == opcodes["eqrr"]:
		if regs[inp1] == regs[inp2]:
			regs[out] = 1
		else:
			regs[out] = 0
		return regs	

regs = [0, 1, 2, 3]
opcodes = {
	"addr": None,
	"addi": None,
	"mulr": None,
	"muli": None,
	"banr": None,
	"bani": None,
	"borr": None,
	"bori": None,
	"setr": None,
	"seti": None,
	"gtir": None,
	"gtri": None,
	"gtrr": None,
	"eqir": None,
	"eqri": None,
	"eqrr": None,
}

count = 0
results = []
inp = open("16.txt").readlines()
for i in range(0, len(inp), 4):
	if inp[i] == "\n": break
	end = {}
	endN = list(map(int, re.findall("-?[0-9]+", inp[i+2].strip())))
	for j in range(len(endN)):
		end[regs[j]] = endN[j]
	instrs = list(map(int, re.findall("-?[0-9]+", inp[i+1].strip())))
	startN = list(map(int, re.findall("-?[0-9]+", inp[i].strip())))
	possible = []
	total = 0
	for opc in opcodes:
		start = {}
		for j in range(len(startN)):
			start[regs[j]] = startN[j]
		start = runProg(start, opc, instrs[1], instrs[2], instrs[3])
		if start == end:
			possible.append(opc)
			total += 1
	possible.append(instrs[0])
	results.append(possible)
	if total >= 3:
		count += 1
print(count)

while None in opcodes.values():
	found = None
	for result in results:
		if len(result) == 2:
			opcodes[result[0]] = result[1]
			found = result[0]
			break
	for result in results:
		if found in result:
			result.remove(found)

regs = {0:0, 1:0, 2:0, 3:0}
for line in inp[3162:]:
	instrs = list(map(int, re.findall("-?[0-9]+", line.strip())))
	regs = runProg(regs, instrs[0], instrs[1], instrs[2], instrs[3])
print(regs[0])