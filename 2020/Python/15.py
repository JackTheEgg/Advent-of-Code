from collections import defaultdict

with open("15.txt") as f:
    inputs = list(map(int, f.read().split(',')))

nums = defaultdict(list)

for i, n in enumerate(inputs):
    nums[n].append(i)

last = n
for i in range(len(inputs), 2020):
    if len(nums[last]) < 2:
        nums[0].append(i)
        last = 0
    else:
        last = nums[last][-1] - nums[last][-2]
        nums[last].append(i)
print(last)

nums = defaultdict(list)

for i, n in enumerate(inputs):
    nums[n].append(i)

last = n
for i in range(len(inputs), 30000000):
    if len(nums[last]) < 2:
        nums[0].append(i)
        last = 0
    else:
        last = nums[last][-1] - nums[last][-2]
        nums[last].append(i)
print(last)