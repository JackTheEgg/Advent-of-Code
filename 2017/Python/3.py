inp = int(open("3.txt").read().strip())

dirs = [(1,0), (0,1), (-1,0), (0,-1)]
x, y, num, times, count, stop = 0, 0, 1, 1, 0, False
while True:
	if stop: break
	for d in dirs:
		if stop: break
		for n in range(times):
			x += d[0]
			y += d[1]
			num += 1
			if num == inp:
				stop = True
				break
		count += 1
		if count == 2:
			times += 1
			count = 0
print(abs(x) + abs(y))

x, y, times, count, stop = 0, 0, 1, 0, False
nums = {(0, 0): 1}
while True:
	if stop: break
	for d in dirs:
		if stop: break
		for n in range(times):
			x += d[0]
			y += d[1]
			nums[(x, y)] = 0
			for i in range(-1, 2):
				for j in range(-1, 2):
					if (x+i, y+j) in nums and not (i == j == 0):
						nums[(x, y)] += nums[(x+i, y+j)]
			if nums[(x, y)] > inp:
				print(nums[(x, y)])
				stop = True
				break
		count += 1
		if count == 2:
			times += 1
			count = 0