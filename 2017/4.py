from itertools import permutations

count = 0
with open("4.txt") as f:
	for line in f:
		words = line.strip().split()
		words2 = set(words)
		if len(words) == len(words2):
			count += 1
print(count)

def isValid(words):
	for i in range(len(words)):
		word = words[i]
		others = [x for n,x in enumerate(words) if n != i]
		ways = list(permutations(list(word)))
		for way in ways:
			if "".join(way) in others:
				return False
	return True

count = 0
with open("4.txt") as f:
	for line in f:
		words = line.strip().split()
		if isValid(words):
			count += 1
print(count)