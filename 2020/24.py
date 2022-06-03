insts = []

with open("24.txt") as f:
    for line in f:
        insts.append(line.strip())

movs = {"w":[-2,0], "e":[2,0], "se":[1,-1], "sw":[-1,-1], "ne":[1,1], "nw":[-1,1]}
startx = 0
starty = 0
turned = []

for inst in insts:
    x = startx
    y = starty
    while inst != "":
        if inst[0] == "e":
            x += movs["e"][0]
            y += movs["e"][1]
            inst = inst[1:]
        elif inst[0] == "w":
            x += movs["w"][0]
            y += movs["w"][1]
            inst = inst[1:]
        elif inst[0:2] == "se":
            x += movs["se"][0]
            y += movs["se"][1]
            inst = inst[2:]
        elif inst[0:2] == "sw":
            x += movs["sw"][0]
            y += movs["sw"][1]
            inst = inst[2:]
        elif inst[0:2] == "nw":
            x += movs["nw"][0]
            y += movs["nw"][1]
            inst = inst[2:]
        elif inst[0:2] == "ne":
            x += movs["ne"][0]
            y += movs["ne"][1]
            inst = inst[2:]
    if not [x, y] in turned:
        turned.append([x, y])
    else:
        turned.remove([x, y])
print(len(turned))

for n in range(100): # bruteforce
    xmin = min(turned[i][0] for i in range(len(turned)))
    xmax = max(turned[i][0] for i in range(len(turned)))
    ymin = min(turned[i][1] for i in range(len(turned)))
    ymax = max(turned[i][1] for i in range(len(turned)))
    turnWhite = []
    turnBlack = []
    for x in range(xmin - 5, xmax + 5):
        for y in range(ymin - 5, ymax + 5):
            if [x, y] in turned:
                count = 0
                for k, v in movs.items():
                    if [x+v[0], y+v[1]] in turned:
                        count += 1
                if count == 0 or count > 2:
                    turnWhite.append([x, y])
            elif [x, y] not in turned:
                count = 0
                for k, v in movs.items():
                    if [x+v[0], y+v[1]] in turned:
                        count += 1
                if count == 2:
                    turnBlack.append([x, y])
    for tile in turnWhite:
        turned.remove(tile)
    for tile in turnBlack:
        turned.append(tile)
print(len(turned))