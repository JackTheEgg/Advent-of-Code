recipes = "37"
e1, e2 = 0, 1
inp = open("14.txt").read().strip()
while not inp in recipes[-7:]:
	score = int(recipes[e1]) + int(recipes[e2])
	recipes += str(score)
	e1 = (e1 + int(recipes[e1]) + 1) % len(recipes)
	e2 = (e2 + int(recipes[e2]) + 1) % len(recipes)
print(recipes[int(inp):int(inp)+10])
if recipes[-6:] == inp:
	print(len(recipes) - 6)
else:
	print(len(recipes) - 7)