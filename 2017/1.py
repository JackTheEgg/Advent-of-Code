inp = open("1.txt").read().strip()

count = 0
for i in range(len(inp)):
	if inp[i % len(inp)] == inp[(i + 1) % len(inp)]:
		count += int(inp[i])
print(count)

half = len(inp) // 2
count = 0
for i in range(len(inp)):
	if inp[i % len(inp)] == inp[(i + half) % len(inp)]:
		count += int(inp[i])
print(count)