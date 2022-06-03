from collections import deque

dirs = {"N":(0,1), "S":(0,-1), "E":(1,0), "W":(-1,0)}
inp = deque(open("20.txt").read()[1:-1])

def branch(x, y, steps):
	x1, y1, steps1 = x, y, steps
	while inp:
		c = inp.popleft()
		if c.isupper():
			x1 += dirs[c][0]
			y1 += dirs[c][1]
			if (x1, y1) in visited:
				continue
			else:
				steps1 += 1
			if steps1 >= 1000:
				part2.add((x1, y1))
			sCount.add(steps1)
			visited.add((x1, y1))
		elif c == "(":
			x1, y1, steps1 = branch(x1, y1, steps1)
		elif c == "|":
			if inp[0] == ")":
				inp.popleft()
				return x, y, steps
			else:
				return branch(x, y, steps)
		elif c == ")":
			return x1, y1, steps1

visited, sCount, part2 = set([(0,0)]), set([0]), set()
branch(0, 0, 0)
print(max(list(sCount)))
print(len(part2))