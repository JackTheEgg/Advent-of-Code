import random

inp = open("19.txt").readlines()
repls = {}
for line in inp:
	if line == "\n":
		break
	else:
		a = line.strip().split(" => ")
		if not a[0] in repls:
			repls[a[0]] = [a[1]]
		else:
			repls[a[0]].append(a[1])
start = inp[-1]
goal = inp[-1]

def changeMol(old, new, start):
	newMols = set()
	indexes = []
	repLen = len(old)
	for ind, char in enumerate(start):
		if char == old[0]:
			indexes.append(ind)
	for ind in indexes:
		if start[ind:ind + repLen] == old:
			newMol = start[:ind] + new + start[ind + repLen:]
			newMols.add(newMol)
	return newMols

newMols = []
for old, news in repls.items():
	for new in news:
		mols = changeMol(old, new, start)
		newMols.append(mols)
newMols = set().union(*newMols)
print(len(newMols))

def step(start): # bruteforce, no funciona
	newMols = []
	for mol in start:
		for old, news in repls.items():
			for new in news:
				mols = changeMol(old, new, mol)
				newMols.append(mols)
	newMols = list(set().union(*newMols))
	return newMols

rep = {}
inv_rep = {}
s = ''
with open('19.txt') as f:
    for line in f.readlines():
        if '=>' in line:
            key, val = line.rstrip().split(' => ')
            inv_rep[val] = key
            if key not in rep:
                rep[key] = []
            rep[key].append(val)                
        else:
            s = line.rstrip()

def backtrack(s, rep):
    count = 0
    old_s = ''
    keys = list(rep.keys())
    random.shuffle(keys)
    while old_s != s:
        old_s = s
        for key in keys:
            while key in s:
                count += s.count(key)
                s = s.replace(key, rep[key])
    return int(s == 'e') * count

p2 = 0
while p2 == 0:
    p2 = backtrack(s, inv_rep)
print(p2)