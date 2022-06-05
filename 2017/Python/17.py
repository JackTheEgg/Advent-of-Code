from collections import deque

steps = int(open("17.txt").read().strip())
lst = deque([0])

for i in range(1, 50000001):
	lst.rotate(-steps)
	lst.append(i)
	if i == 2017:
		print(lst[0])
print(lst[lst.index(0) + 1])