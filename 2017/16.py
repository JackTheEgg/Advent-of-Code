from collections import deque

def swapLet(lst, let1, let2):
	ind1 = lst.index(let1)
	ind2 = lst.index(let2)
	lst[ind1] = let2
	lst[ind2] = let1
	return lst

def swapInd(lst, ind1, ind2):
	let1 = lst[ind1]
	let2 = lst[ind2]
	lst[ind1] = let2
	lst[ind2] = let1
	return lst

steps = open("16.txt").read().strip().split(",")
progs = deque(list("abcdefghijklmnop"))
seq = ["".join(progs)]
for n in range(1000):
	for step in steps:
		if step[0] == "s":
			progs.rotate(int(step[1:]))
		elif step[0] == "x":
			ind1, ind2 = step[1:].split("/")
			progs = swapInd(progs, int(ind1), int(ind2))
		elif step[0] == "p":
			let1, let2 = step[1:].split("/")
			progs = swapLet(progs, let1, let2)
	if "".join(progs) in seq:
		break
	else:
		seq.append("".join(progs))

print(seq[1])
print(seq[1000000000 % len(seq)])