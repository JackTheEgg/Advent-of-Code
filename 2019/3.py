wires = []
with open("3.txt") as f:
    for line in f:
        wire = line.strip().split(",")
        wires.append(wire)

wirepoints = []
for wire in wires:
    x = 0
    y = 0
    points = [(0, 0)]
    for inst in wire:
        if inst[0] == "R":
            x += int(inst[1:])
            points.append((x, y))
        elif inst[0] == "L":
            x -= int(inst[1:])
            points.append((x, y))
        elif inst[0] == "U":
            y += int(inst[1:])
            points.append((x, y))
        elif inst[0] == "D":
            y -= int(inst[1:])
            points.append((x, y))
    wirepoints.append(points)

def line_intersect(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    d = (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)
    if d:
        uA = ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d
        uB = ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d
    else:
        return
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
    x = Ax1 + uA * (Ax2 - Ax1)
    y = Ay1 + uA * (Ay2 - Ay1)
    return (round(x), round(y))

intersects = []
for i in range(1, len(wirepoints[0])):
    for j in range(1, len(wirepoints[1])):
        (a, b), (c, d) = wirepoints[0][i-1], wirepoints[0][i] 
        (e, f), (g, h) = wirepoints[1][j-1], wirepoints[1][j]  
        pt = line_intersect(a, b, c, d, e, f, g, h)
        if pt and not pt in intersects and not pt == (0, 0):
            intersects.append(pt)

dists = []
for inters in intersects:
    dist = abs(inters[0]) + abs(inters[1])
    dists.append(dist)
dists.sort()
print(dists[0])

steps = {}
for inters in intersects:
    steps[inters] = 0

for wire in wires:
    x = 0
    y = 0
    step = 0
    for inst in wire:
        if inst[0] == "R":
            for i in range(int(inst[1:])):
                x += 1
                step += 1
                if (x, y) in steps:
                    steps[(x, y)] += step
        elif inst[0] == "L":
            for i in range(int(inst[1:])):
                x -= 1
                step += 1
                if (x, y) in steps:
                    steps[(x, y)] += step
        elif inst[0] == "U":
            for i in range(int(inst[1:])):             
                y += 1
                step += 1
                if (x, y) in steps:
                    steps[(x, y)] += step
        elif inst[0] == "D":
            for i in range(int(inst[1:])):            
                y -= 1
                step += 1
                if (x, y) in steps:
                    steps[(x, y)] += step

totSteps = []
for k, v in steps.items():
    totSteps.append(v)
totSteps.sort()
print(totSteps[0])