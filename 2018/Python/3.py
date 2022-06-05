import re

grid = [[0 for x in range(1000)] for y in range(1000)]
with open("3.txt") as f:
	for line in f:
		nums = list(map(int, re.findall("-?[0-9]+", line.strip())))
		y, x = nums[2], nums[1]
		for i in range(nums[3]):
			for j in range(nums[4]):
				grid[y+j][x+i] += 1
print(sum(grid[y][x] >= 2 for y in range(1000) for x in range(1000)))

def isAlone(x, y, w, h):
	for i in range(w):
		for j in range(h):
			if grid[y+j][x+i] >= 2:
				return False
	return True

with open("3.txt") as f:
	for line in f:
		nums = list(map(int, re.findall("-?[0-9]+", line.strip())))
		x, y, w, h = nums[1], nums[2], nums[3], nums[4]
		if isAlone(x, y, w, h):
			print(nums[0])
			break