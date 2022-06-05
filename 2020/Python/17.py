from itertools import product

def get_bounds(cells):
    res = []
    for i in range(4):
        res.append(min(cells, key=lambda x: x[i])[i] - 1)
        res.append(max(cells, key=lambda x: x[i])[i] + 2)
    return res

def step(cells, d=3):
    bounds = get_bounds(cells)
    next_cells = set()
    w_range = [0] if d == 3 else range(bounds[6], bounds[7])
    for x in range(bounds[0], bounds[1]):
        for y in range(bounds[2], bounds[3]):
            for z in range(bounds[4], bounds[5]):
                for w in w_range:
                    ns = get_n_count((x, y, z, w), cells)
                    if (x, y, z, w) in cells and (ns == 2 or ns == 3):
                        next_cells.add((x, y, z, w))
                    elif (x, y, z, w) not in cells and ns == 3:
                        next_cells.add((x, y, z, w))
    return next_cells

def get_n_count(point, cells):
    dim = len(point)
    diffs = product([-1, 0, 1], repeat=dim)
    return sum(
        [
            tuple([x1 + x2 for x1, x2 in zip(d, point)]) in cells
            for d in diffs
            if d != tuple([0] * dim)
        ]
    )

with open("17.txt") as f:
    raw_in = f.readlines()

cells = set()

for y, line in enumerate(raw_in):
    for x, cell in enumerate(line):
        if cell == "#":
            cells.add((x, y) + (0,) * 2)

p1 = cells.copy()
for _ in range(6):
    p1 = step(p1)
print(len(p1))

p2 = cells.copy()
for _ in range(6):
    p2 = step(p2, d=4)
print(len(p2))