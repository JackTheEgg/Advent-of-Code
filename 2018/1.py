import sys

inp = list(map(int, open("1.txt").read().splitlines()))
print(sum(inp))

outs = []
count = 0
while True:
	for num in inp:
		count += num
		if not count in outs:
			outs.append(count)
		else:
			print(count)
			sys.exit()