import hashlib

def	genPaths(paths):
	nextPaths = set()
	for path in paths:
		test = inp + path[2]
		result = hashlib.md5(test.encode()).hexdigest()
		possible = set()
		for ind, char in enumerate(result[:4]):
			if (path[0] + dirs[ind][0], path[1] + dirs[ind][1]) in valid and char in opened:
				possible.add((path[0] + dirs[ind][0], path[1] + dirs[ind][1], path[2] + dirs[ind][2]))
		for mov in possible:
			if mov[0] == 3 and mov[1] == -3:
				endPaths.add(mov[2])
			else:
				nextPaths.add(mov)
	return nextPaths

valid = [(x,-y) for x in range(4) for y in range(4)]
opened = "bcdef"
inp = open("17.txt").read().strip()
dirs = [(0,1,"U"), (0,-1,"D"), (-1,0,"L"), (1,0,"R")]
endPaths = set()
paths = set()
paths.add((0, 0, ""))

while len(paths) != 0:
	paths = genPaths(paths)

endPaths = sorted(list(endPaths), key = len)
print(endPaths[0])
print(len(endPaths[-1]))