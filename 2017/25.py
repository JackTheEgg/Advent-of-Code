inp = open("25.txt").readlines()

insts = {}
L = 9
state = [0]
cond = [1, 5]
info = [2, 3, 4, 6, 7, 8]
for i, line in enumerate(inp[3:]):
	if i % L in state:
		let = line.strip().split()[-1][0]
		insts[let] = {}
	elif i % L in cond:
		num = int(line.strip().split()[-1][0])
		insts[let][num] = []
	elif i % L in info:
		insts[let][num].append(line.strip().split()[-1][:-1])

state = "A"
steps = 12667664
tape = {x:0 for x in range(-10000, 10000)}
x = 0
for n in range(steps):
	act = insts[state][tape[x]]
	tape[x] = int(act[0])
	if act[1] == "right":
		x += 1
	else:
		x -= 1
	state = act[2]
print(sum(tape.values()))