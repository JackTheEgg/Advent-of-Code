from string import ascii_lowercase
import sys

letters = ascii_lowercase
def doubles(s):
	for letter in letters:
		if s.count(letter) == 2:
			return True
	return False

def triples(s):
	for letter in letters:
		if s.count(letter) == 3:
			return True
	return False

d, t = 0, 0
with open("2.txt") as f:
	for line in f:
		s = line.strip()
		if doubles(s):
			d += 1
		if triples(s):
			t += 1
print(d*t)

IDs = open("2.txt").read().splitlines()
for i in range(len(IDs)):
	test = IDs[i]
	others = [x for n, x in enumerate(IDs) if n != i]
	for other in others:
		count = 0
		for j in range(len(other)):
			if other[j] != test[j]:
				point = j
				count += 1
		if count == 1:
			print(test[:point] + test[point+1:])
			sys.exit()