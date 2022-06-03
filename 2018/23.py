import re
from queue import PriorityQueue

bots = {}
with open("23.txt") as f:
	for i, line in enumerate(f):
		nums = list(map(int, re.findall("-?[0-9]+", line.strip())))
		bots[i] = {"p": tuple(nums[0:3]), "r":nums[-1]}

best = None
for n, info in bots.items():
	if info["r"] == max(i["r"] for i in bots.values()):
		best = n
		break

count = 0
for bot, info in bots.items():
	dist = sum(map(abs, [bots[best]["p"][i] - info["p"][i] for i in range(3)]))
	if dist <= bots[best]["r"]:
		count += 1
print(count)

bots = [map(int, re.findall("-?\d+", line)) for line in open("23.txt").readlines()]
q = PriorityQueue()
for x,y,z,r in bots:
  	d = abs(x) + abs(y) + abs(z)
  	q.put((max(0, d - r),1))
  	q.put((d + r + 1,-1))
count = 0
maxCount = 0
result = 0
while not q.empty():
  	dist,e = q.get()
  	count += e
  	if count > maxCount:
  	  	result = dist
  	  	maxCount = count
print(result)