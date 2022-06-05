scanners = {}
with open("13.txt") as f:
	for line in f:
		i = line.strip().split(": ")
		scanners[int(i[0])] = 2*int(i[1]) - 2

def isValid(num, part1 = False):
	for n, L in scanners.items():
		if (n + num) % L == 0:
			if part1:
				sev.append(((L + 2) // 2) * n)
			else:
				return False
	return True

sev = []
isValid(0, True)
print(sum(sev))

for t in range(100000000000000):
	if isValid(t):
		print(t)
		break