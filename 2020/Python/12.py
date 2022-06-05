steps = []
with open("12.txt") as file:
    for line in file:
        steps.append(line.strip())

left = { 90: { "N":"W", "W":"S", "S":"E", "E":"N" }, 180: { "N":"S", "S":"N", "E":"W", "W":"E" }, 270: { "N":"E", "W":"N", "S":"W", "E":"S"} }
right = { 90: { "N":"E", "W":"N", "S":"W", "E":"S" }, 180: { "N":"S", "S":"N", "E":"W", "W":"E" }, 270: { "N":"W", "W":"S", "S":"E", "E":"N"} }
face = "E"
x = 0
y = 0
for step in steps:
    if step[0] == "N":
        y += int(step[1:])
    elif step[0] == "S":
        y -= int(step[1:])
    elif step[0] == "E":
        x += int(step[1:])
    elif step[0] == "W":
        x -= int(step[1:])
    elif step[0] == "L":
        face = left[int(step[1:])][face]
    elif step[0] == "R":
        face = right[int(step[1:])][face]
    elif step[0] == "F":
        if face == "N":
            y += int(step[1:])
        elif face == "S":
            y -= int(step[1:])
        elif face == "E":
            x += int(step[1:])
        elif face == "W":
            x -= int(step[1:])
print(abs(x) + abs(y))

def rotate(way, deg, startx, starty):
    x = 0
    y = 0
    if way == "R":
        if deg == 90:
            x = starty
            y = -startx
        elif deg == 180:
            x = -startx
            y = -starty
        elif deg == 270:
            x = -starty
            y = startx
    elif way == "L":
        if deg == 90:
            x = -starty
            y = startx
        elif deg == 180:
            x = -startx
            y = -starty
        elif deg == 270:
            x = starty
            y = -startx
    return x, y

x = 0
y = 0
pointx = 10
pointy = 1
for step in steps:
    if step[0] == "N":
        pointy += int(step[1:])
    elif step[0] == "S":
        pointy -= int(step[1:])
    elif step[0] == "E":
        pointx += int(step[1:])
    elif step[0] == "W":
        pointx -= int(step[1:])
    elif step[0] == "L" or step[0] == "R":
        pointx, pointy = rotate(step[0], int(step[1:]), pointx, pointy)
    elif step[0] == "F":
        x += int(step[1:]) * pointx
        y += int(step[1:]) * pointy
print(abs(x) + abs(y))