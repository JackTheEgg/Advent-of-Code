inp = open("9.txt").read().strip()

score, gScore, i, garbage = 0, 0, 0, False
while i <= len(inp) - 1:
	if inp[i] == "{" and not garbage:
		gScore += 1
		i += 1
	elif inp[i] == "}" and not garbage:
		score += gScore
		gScore -= 1
		i += 1
	elif inp[i] == "<":
		garbage = True
		i += 1
	elif inp[i] == ">" and garbage:
		garbage = False
		i += 1
	elif inp[i] == "!":
		i += 2
	else:
		i += 1
print(score)

i, garbage, gScore = 0, False, 0
while i <= len(inp) - 1:
	if inp[i] == "<" and not garbage:
		garbage = True
		i += 1
	elif inp[i] == ">" and garbage:
		garbage = False
		i += 1
	elif inp[i] == "!":
		i += 2
	elif garbage:
		gScore += 1
		i += 1
	else:
		i += 1
print(gScore)