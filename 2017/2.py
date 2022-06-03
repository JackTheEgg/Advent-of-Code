count = 0
with open("2.txt") as f:
	for line in f:
		nums = list(map(int, line.strip().split()))
		count += max(nums) - min(nums)
print(count)

count = 0
with open("2.txt") as f:
	for line in f:
		nums = list(map(int, line.strip().split()))
		for i in range(len(nums)):
			num = nums[i]
			othernums = [x for n, x in enumerate(nums) if n != i]
			for other in othernums:
				if num % other == 0:
					count += num // other
print(count)