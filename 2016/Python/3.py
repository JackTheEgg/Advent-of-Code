count = 0
nums = []
with open("3.txt") as f:
	for line in f:
		sideCount = 0
		inp = list(map(int, line.strip().split()))
		nums.append(inp)
		for i in range(len(inp)):
		    side = inp[i]
		    othersides = [x for n, x in enumerate(inp) if n != i]
		    if sum(othersides) > side:
		    	sideCount += 1
		if sideCount == 3:
			count += 1
print(count)

count = 0
for y in range(0, len(nums), 3):
	for x in range(3):
		sideCount = 0
		inp = [nums[y+i][x] for i in range(3)]
		for i in range(len(inp)):
		    side = inp[i]
		    othersides = [j for n, j in enumerate(inp) if n != i]
		    if sum(othersides) > side:
		    	sideCount += 1
		if sideCount == 3:
			count += 1
print(count)