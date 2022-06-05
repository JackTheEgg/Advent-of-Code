import string

letters = string.ascii_lowercase
pairs = []
abas = []
babs = []
for i in range(len(letters)):
    letter = letters[i]
    otherletters = [x for n, x in enumerate(letters) if n != i]
    for other in otherletters:
    	pairs.append(letter + 2*other + letter)
    	abas.append(letter + other + letter)
    	babs.append(other + letter + other)

def isValid1(tbl):
	count = 0
	for pair in pairs:
		for i in range(0, len(tbl), 2):
			if pair in tbl[i]:
				count += 1
	if count == 0: 
		return False
	for pair in pairs:
		for i in range(1, len(tbl), 2):
			if pair in tbl[i]:
				return False
	return True

def isValid2(tbl):
	count = 0
	for i in range(len(abas)):
		for j in range(0, len(tbl), 2):
			if abas[i] in tbl[j]:
				for k in range(1, len(tbl), 2):
					if babs[i] in tbl[k]:
						count += 1
	if count >= 1:
		return True
	else:
		return False

countp1 = 0
countp2 = 0
with open("7.txt") as f:
	for line in f:
		inp = line.strip().split(" ")
		if isValid1(inp):
			countp1 += 1
		if isValid2(inp):
			countp2 += 1
print(countp1)
print(countp2)