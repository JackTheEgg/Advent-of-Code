import numpy as np
import sys

def power(x, y):
	rID = x + 10
	pw = rID * y 
	pw += inp
	pw *= rID
	pw = (pw % 1000) // 100
	return pw - 5

inp = int(open("11.txt").read().strip())

grid = {}
for y in range(1, 301):
	for x in range(1, 301):
		grid[(x,y)] = power(x,y)

def buildSquares(x, y):
	size = 1
	squares = {}
	while (x + size - 1 <= 300) and (y + size - 1 <= 300):
		squares[size] = sum([grid[(x+i, y+j)] for i in range(size) for j in range(size)])
		size += 1
	return squares

corners = {}
for coord in grid:
	corners[coord] = buildSquares(coord[0], coord[1]) # bruteforce

squares3 = []
for pair, squares in corners.items():
	if 3 in squares:
		squares3.append(squares[3])
for pair, squares in corners.items():
	if 3 in squares:
		if squares[3] == max(squares3):
			print(str(pair[0]) + "," + str(pair[1]))
			break

maxVal = np.max([list(i.values()) for i in list(corners.values())])
for pair, squares in corners.items():
	for size, val in squares.items():
		if val == maxVal:
			print(str(pair[0]) + "," + str(pair[1]) + "," + str(size))
			sys.exit()