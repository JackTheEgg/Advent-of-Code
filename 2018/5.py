from string import ascii_lowercase, ascii_uppercase

U = ascii_uppercase
L = ascii_lowercase
pairs = [U[i] + L[i] for i in range(len(U))]
p = open("5.txt").read().strip()
p2 = p

def shorten(p):
	while True:
		check = len(p)
		for pair in pairs:
			if pair in p:
				p = p.replace(pair, "")
			if pair[::-1] in p:
				p = p.replace(pair[::-1], "")
		if check == len(p):
			return p

print(len(shorten(p)))

lengths = []
for i in range(len(U)):
	test = str(p2)
	test = test.replace(U[i], "")
	test = test.replace(L[i], "")
	lengths.append(len(shorten(test)))
print(min(lengths))