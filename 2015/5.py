vowels = ["a", "e", "i", "o", "u"]
letters = "abcdefghijklmnopqrstuvwxyz"
badstrings = ["ab", "cd", "pq", "xy"]
triples = [3*s for s in letters]

def isGoodv1(s):
	vowelCount = 0
	for char in s:
		if char in vowels:
			vowelCount += 1
	if vowelCount < 3:
		return False
	doubleCount = 0
	for char in letters:
		if char + char in s:
			doubleCount += 1
	if doubleCount < 1:
		return False
	for badstring in badstrings:
		if badstring in s:
			return False
	return True

def isGoodv2(s):
	doubles = {}
	doubleCount = 0
	for i in range(len(s) - 1):
		if not s[i] + s[i+1] in doubles:
			doubles[s[i] + s[i+1]] = 1
		else:
			doubles[s[i] + s[i+1]] += 1
	for trip in triples:
		if trip in s:
			doubles[trip[1:]] -= 1
	for k in doubles:
		if doubles[k] >= 2:
			doubleCount += 1
	if doubleCount == 0:
		return False 
	between = 0
	for i in range(1, len(s) - 1):
		if s[i-1] == s[i+1]:
			between += 1
	if between == 0:
		return False
	return True

countp1, countp2 = 0, 0
with open("5.txt") as f:
	for line in f:
		if isGoodv1(line.strip()):
			countp1 += 1
		if isGoodv2(line.strip()):
			countp2 += 1
print(countp1)
print(countp2)