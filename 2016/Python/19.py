maxElves = int(open("19.txt").read().strip())

def steal1(lst):
	if len(lst) % 2 == 0:
		return [lst[i] for i in range(0, len(lst), 2)]
	else:
		return [lst[i] for i in range(2, len(lst), 2)]

elves = [i for i in range(1, maxElves + 1)]
while len(elves) != 1:
	elves = steal1(elves)
print(elves[0])

def steal2(i, target):
	while i * 3 < target:
		i *= 3
	return target - i

print(steal2(1, maxElves))