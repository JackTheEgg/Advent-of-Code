from itertools import permutations

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

def move(lst, ind1, ind2):
	let = lst.pop(ind1)
	lst.insert(ind2, let)
	return lst

def rotSteps(lst, steps, way):
	newlst = lst.copy()
	if way == "right":
		for ind, char in enumerate(lst):
			newlst[(ind + steps) % len(lst)] = char
		return newlst
	elif way == "left":
		for ind, char in enumerate(lst):
			newlst[(ind - steps) % len(lst)] = char
		return newlst

def rotPos(lst, let):
	steps = lst.index(let)
	if steps >= 4:
		return rotSteps(lst, 1 + steps + 1, "right")
	else:
		return rotSteps(lst, 1 + steps, "right")

def reverse(lst, ind1, ind2):
	if ind1 == 0:
		return lst[:0] + lst[ind2::-1] + lst[ind2+1:]
	else:
		return lst[:ind1] + lst[ind2:ind1-1:-1] + lst[ind2+1:]

f = open("21.txt").readlines() 

lst = list("abcdefgh")
for line in f:
	inp = line.strip().split(" ")
	if inp[0] == "swap":
		if inp[1] == "position":
			lst = swapInd(lst, int(inp[2]), int(inp[5]))
		elif inp[1] == "letter":
			lst = swapLet(lst, inp[2], inp[5])
	elif inp[0] == "move":
		lst = move(lst, int(inp[2]), int(inp[5]))
	elif inp[0] == "reverse":
		lst = reverse(lst, int(inp[2]), int(inp[4]))
	elif inp[0] == "rotate":
		if inp[1] == "left" or inp[1] == "right":
			lst = rotSteps(lst, int(inp[2]), inp[1])
		else:
			lst = rotPos(lst, inp[6])
print("".join(lst))

ways = list(permutations(list("abcdefgh")))
final = list("fbgdceah")
for way in ways:
	original = list(way).copy()
	way = list(way)
	for line in f:
		inp = line.strip().split(" ")
		if inp[0] == "swap":
			if inp[1] == "position":
				way = swapInd(way, int(inp[2]), int(inp[5]))
			elif inp[1] == "letter":
				way = swapLet(way, inp[2], inp[5])
		elif inp[0] == "move":
			way = move(way, int(inp[2]), int(inp[5]))
		elif inp[0] == "reverse":
			way = reverse(way, int(inp[2]), int(inp[4]))
		elif inp[0] == "rotate":
			if inp[1] == "left" or inp[1] == "right":
				way = rotSteps(way, int(inp[2]), inp[1])
			else:
				way = rotPos(way, inp[6])
	if way == final:
		print("".join(original))
		break