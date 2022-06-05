nums = list(map(int, open("6.txt").read().split()))
seen = [nums]
steps = 0
while True:
	nums = nums.copy()
	steps += 1
	i = nums.index(max(nums))
	amount = nums[i]
	nums[i] = 0
	a = 1
	while amount != 0:
		nums[(i+a) % len(nums)] += 1
		amount -= 1
		a += 1
	if nums in seen:
		numsp2 = nums.copy()
		break
	else:
		seen.append(nums)
print(steps)

seen = [numsp2]
steps2 = 0
while True:
	numsp2 = numsp2.copy()
	steps2 += 1
	i = numsp2.index(max(numsp2))
	amount = numsp2[i]
	numsp2[i] = 0
	a = 1
	while amount != 0:
		numsp2[(i+a) % len(numsp2)] += 1
		amount -= 1
		a += 1
	if numsp2 in seen:
		break
	else:
		seen.append(numsp2)
print(steps2)