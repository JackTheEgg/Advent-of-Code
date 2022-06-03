import string

alph = string.ascii_lowercase

def isValid(code, letters):
	check = 1000
	for i in range(len(letters)):
		if not letters[i] in code:
			return False
		elif code.count(letters[i]) > check:
			return False
		elif code.count(letters[i]) < check:
			check = code.count(letters[i])
		elif code.count(letters[i]) == check:
			if alph.index(letters[i]) < alph.index(letters[i-1]):
				return False
			else:
				check = code.count(letters[i])
	return True

def decypher(code):
	shift = int(code[-1])
	message = ""
	for word in code[:-1]:
		newWord = ""
		for letter in word:
			newWord += alph[(alph.index(letter) + shift) % len(alph)]
		message += newWord + " "
	return message

count = 0
with open("4.txt") as f:
	for line in f:
		info, letters = line.strip().split(" ")
		vals = info.split("-")
		code = "".join(vals[:-1])
		if isValid(code, letters):
			message = decypher(vals)
			if "north" in message:
				print(int(vals[-1]))
			count += int(vals[-1])
print(count)