import string

letters = string.ascii_lowercase
nextLetter = {letters[i]: letters[i+1] for i in range(len(letters) - 1)}
triples = [letters[i:i+3] for i in range(len(letters) - 2)]
pairs = [2*letter for letter in letters]
def nextPassword(s):
	if s[-1] != "z":
		return s[:-1] + nextLetter[s[-1]]
	else:
		if s[-2] != "z":
			return s[:-2] + nextLetter[s[-2]] + "a"
		else:
			if s[-3] != "z":
				return s[:-3] + nextLetter[s[-3]] + "aa"	
			else:
				if s[-4] != "z":
					return s[:-4] + nextLetter[s[-4]] + "aaa"
				else:
					if s[-5] != "z":
						return s[:-5] + nextLetter[s[-5]] + "aaaa"
					else:
						if s[-6] != "z":
							return s[:-6] + nextLetter[s[-6]] + "aaaaa"
						else:
							if s[-7] != "z":
								return s[:-7] + nextLetter[s[-7]] + "aaaaaa"
							else:
								if s[-8] != "z":
									return s[:-8] + nextLetter[s[-8]] + "aaaaaaa"

def isGood(s):
	if sum(triples[i] in s for i in range(len(triples))) == 0:
		return False
	if (("i" in s) or ("o" in s) or ("l" in s)):
		return False
	count = 0
	for pair in pairs:
		if pair in s:
			count += 1
	if count < 2:
		return False
	return True

password = open("11.txt").read().strip()

passCount = 0
while passCount < 2:
	if isGood(password) and passCount == 0:
		print(password)
		pass1 = password
		passCount += 1
	elif passCount == 1:
		if isGood(password) and password != pass1:
			print(password)
			passCount += 1
		else:
			password = nextPassword(password)	
	else:
		password = nextPassword(password)