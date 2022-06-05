prog = list(map(int, open("5.txt").read().splitlines()))

i, steps = 0, 0
prog1 = prog.copy()
while i <= len(prog1) - 1:
	steps += 1
	prev = i
	i += prog1[i]
	prog1[prev] += 1
print(steps)

i, steps = 0, 0
prog2 = prog.copy()
while i <= len(prog2) - 1:
	steps += 1
	prev = i
	i += prog2[i]
	if prog2[prev] >= 3:
		prog2[prev] -= 1
	else:
		prog2[prev] += 1
print(steps)