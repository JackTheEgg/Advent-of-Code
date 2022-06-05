from functools import reduce
from operator import xor

def step(lst, size, i, skipSize):
	L = len(lst)
	frag = [lst[(i + n) % L] for n in range(size)]
	frag.reverse()
	for n in range(size):
		lst[(i + n) % L] = frag[n]
	i += (size + skipSize) % L 
	skipSize += 1
	return lst, i, skipSize

lst = [i for i in range(256)]
steps = list(map(int, open("10.txt").read().strip().split(",")))
i, skipSize = 0, 0
for num in steps:
	lst, i, skipSize = step(lst, num, i, skipSize)
print(lst[0]*lst[1])

lst = [i for i in range(256)]
inp = open("10.txt").read().strip()
seq = [ord(char) for char in inp] + [17, 31, 73, 47, 23]

i, skipSize = 0, 0
for n in range(64):
	for num in seq:
		lst, i, skipSize = step(lst, num, i, skipSize)

dHash = []
for i in range(0, len(lst), 16):
	dHash.append(reduce(xor, lst[i:i+16]))

s = ""
for num in dHash:
	s += hex(num)[2:]
print(s)