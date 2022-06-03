buttons = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]

minX, minY, maxX, maxY = 0, 0, 2, 2
x, y = 1, 1
code = ""
with open("2.txt") as f:
	for line in f:
		for char in line.strip():
			if char == "U" and y > minY:
				y -= 1
			elif char == "D" and y < maxY:
				y += 1
			elif char == "R" and x < maxX:
				x += 1
			elif char == "L" and x > minX:
				x -= 1
		code += str(buttons[y][x])
print(code)

buttons = [
  ["", "", 1, "", ""],
  ["", 2, 3, 4, ""],
  [5, 6, 7, 8, 9],
  ["", "A", "B", "C", ""],
  ["", "", "D", "", ""]
]

canMove = { 
	"U": {(0, 2):False, (1, 1):False, (1, 2):True, (1, 3):False, (2, 0):False, (2, 1):True, (2, 2):True, (2, 3):True, (2, 4):False, (3, 1):True, (3, 2):True, (3, 3):True, (4, 2):True},
	"D": {(0, 2):True, (1, 1):True, (1, 2):True, (1, 3):True, (2, 0):False, (2, 1):True, (2, 2):True, (2, 3):True, (2, 4):False, (3, 1):False, (3, 2):True, (3, 3):False, (4, 2):False},
	"R": {(0, 2):False, (1, 1):True, (1, 2):True, (1, 3):False, (2, 0):True, (2, 1):True, (2, 2):True, (2, 3):True, (2, 4):False, (3, 1):True, (3, 2):True, (3, 3):False, (4, 2):False},
	"L": {(0, 2):False, (1, 1):False, (1, 2):True, (1, 3):True, (2, 0):False, (2, 1):True, (2, 2):True, (2, 3):True, (2, 4):True, (3, 1):False, (3, 2):True, (3, 3):True, (4, 2):False},
}

y, x = 2, 0
code = ""
with open("2.txt") as f:
	for line in f:
		for char in line.strip():
			if char == "U" and canMove[char][(y, x)]:
				y -= 1
			elif char == "D" and canMove[char][(y, x)]:
				y += 1
			elif char == "R" and canMove[char][(y, x)]:
				x += 1
			elif char == "L" and canMove[char][(y, x)]:
				x -= 1
		code += str(buttons[y][x])
print(code)