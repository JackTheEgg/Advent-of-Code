import math
import copy
from collections import defaultdict
import numpy as np

def dist(a1, a2):
    return math.sqrt(pow(a1[0] - a2[0], 2) + pow(a1[1] - a2[1], 2))

with open("10.txt") as f:
    lines = list(map(str.strip, f.readlines()))

asteroids = []
for y, line in enumerate(lines):
    for x, xval in enumerate(line):
        if xval == "#":
            asteroids.append((x, y))

def dotP(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

grid = []
coords = []
with open("10.txt") as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(char)
        grid.append(row)

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "#":
            coords.append((x, -y)) # x increases to the right, y decreases going down

astCount = []
for i in range(len(coords)):
    ast = coords[i]
    otherasts = [x for n, x in enumerate(coords) if n != i]
    vectors = []
    for coord in otherasts:
        vector = (coord[0] - ast[0], coord[1] - ast[1])
        vectors.append(vector)
    test = copy.deepcopy(vectors)
    while len(test) > 0:
        cands = []
        vec = test.pop(0)
        for a in test:
            if round(dotP(vec, a)/(np.linalg.norm(a)*np.linalg.norm(vec)), 7) == 1:
                cands.append(a)
        for cand in cands:
            test.remove(cand)
            vectors.remove(cand)
    visible = len(vectors)
    astCount.append(visible)
    if visible == 329: #<<< solution problem 1 >>>
        break
astCount.sort()
print(astCount[-1])

base = (25, 31)
asteroids.remove(base)
angles = defaultdict(list)
for ast in asteroids:
    if ast == base:
        continue
    angle = (math.degrees(math.atan2(ast[1] - base[1], ast[0] - base[0])) + 90) % 360
    angles[angle].append((dist(ast, base), ast))

for angle in angles:
    angles[angle] = sorted(angles[angle], reverse=True)

i = 0
for angle in sorted(angles):
    boom = angles[angle].pop()
    i += 1
    if i == 200:
        result = boom[1]
        break
print(result[0]*100 + result[1])