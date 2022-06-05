with open("11.txt") as f:
    for line in f:
        prog = list(map(int, line.strip().split(",")))

for i in range(100000):
    prog.append(0)

def getValues(prog, ind, relBase):
    if str(prog[ind])[-3] == "1":
        value1 = prog[ind + 1]
    elif str(prog[ind])[-3] == "2":
        value1 = prog[prog[ind + 1] + relBase]
    else:
        value1 = prog[prog[ind + 1]]
    if len(str(prog[ind])) >= 4:    
        if str(prog[ind])[-4] == "1":
            value2 = prog[ind + 2]
        elif str(prog[ind])[-4] == "2":
            value2 = prog[prog[ind + 2] + relBase]
        else:
            value2 = prog[prog[ind + 2]]
    else:
        value2 = prog[prog[ind + 2]]
    return value1, value2

def getPosition(prog, ind, relBase):
    if len(str(prog[ind])) > 4:
        if str(prog[ind])[-5] == "2":
            pos = prog[ind + 3] + relBase
        else:
            pos = prog[ind + 3]
    else:
        pos = prog[ind + 3]
    return pos

def runProgv5(prog, ind, relBase, inp, inpInd, out, useLoop = False):
    while True:
        if prog[ind] == 99: # value 99
            return "Program finished", ind, relBase
        elif prog[ind] == 1: # value 1 (simple)
            prog[prog[ind + 3]] = prog[prog[ind + 2]] + prog[prog[ind + 1]]
            ind += 4
        elif prog[ind] == 2: # value 2 (simple)
            prog[prog[ind + 3]] = prog[prog[ind + 2]] * prog[prog[ind + 1]]
            ind += 4
        elif prog[ind] == 3: # value 3 (simple)
            prog[prog[ind + 1]] = inp[inpInd]
            ind += 2
        elif prog[ind] == 4: # value 4 (simple)
            output = prog[prog[ind + 1]]
            ind += 2
            out.append(output)
            if useLoop:
                return prog, ind, relBase
            else:
                return
        elif prog[ind] == 5: # value 5 (simple)
            if prog[prog[ind + 1]] != 0:
                ind = prog[prog[ind + 2]]
            else:
                ind += 3
        elif prog[ind] == 6: # value 6 (simple)
            if prog[prog[ind + 1]] == 0:
                ind = prog[prog[ind + 2]]
            else:
                ind += 3
        elif prog[ind] == 7: # value 7 (simple)
            if prog[prog[ind + 1]] < prog[prog[ind + 2]]:
                prog[prog[ind + 3]] = 1
            else:
                prog[prog[ind + 3]] = 0
            ind += 4
        elif prog[ind] == 8: # value 8 (simple)
            if prog[prog[ind + 1]] == prog[prog[ind + 2]]:
                prog[prog[ind + 3]] = 1
            else:
                prog[prog[ind + 3]] = 0
            ind += 4
        elif prog[ind] == 9: # value 9 (simple)
            relBase += prog[prog[ind + 1]]
            ind += 2
        elif str(prog[ind])[-2:] == "01": # value 1 (complex 0, 1, 2)
            value1, value2 = getValues(prog, ind, relBase)
            pos = getPosition(prog, ind, relBase)
            prog[pos] = value1 + value2
            ind += 4
        elif str(prog[ind])[-2:] == "02": # value 2 (complex 0, 1, 2)
            value1, value2 = getValues(prog, ind, relBase)
            pos = getPosition(prog, ind, relBase)
            prog[pos] = value1 * value2
            ind += 4
        elif str(prog[ind])[-2:] == "03": # value 3 (complex 1, 2)
            if str(prog[ind])[-3] == "2":
                prog[prog[ind + 1] + relBase] = inp[inpInd]
            else:
                prog[ind + 1] = inp[inpInd]
            ind += 2
        elif str(prog[ind])[-2:] == "04": # value 4 (complex 1, 2)
            if str(prog[ind])[-3] == "1":
                output = prog[ind + 1]
            else:
                output = prog[prog[ind + 1] + relBase]
            ind += 2
            out.append(output)
            if useLoop:
                return prog, ind, relBase
            else:
                return 
        elif str(prog[ind])[-2:] == "05": # value 5 (complex 0, 1, 2)
            value1, value2 = getValues(prog, ind, relBase)
            if value1 != 0:
                ind = value2
            else:
                ind += 3
        elif str(prog[ind])[-2:] == "06": # value 6 (complex 0, 1, 2)
            value1, value2 = getValues(prog, ind, relBase)
            if value1 == 0:
                ind = value2
            else:
                ind += 3
        elif str(prog[ind])[-2:] == "07": # value 7 (complex 0, 1, 2)
            value1, value2 = getValues(prog, ind, relBase)
            if value1 < value2:
                pos = getPosition(prog, ind, relBase)
                prog[pos] = 1
            else:
                pos = getPosition(prog, ind, relBase)
                prog[pos] = 0
            ind += 4
        elif str(prog[ind])[-2:] == "08": # value 8 (complex 0, 1, 2)
            value1, value2 = getValues(prog, ind, relBase)
            if value1 == value2:
                pos = getPosition(prog, ind, relBase)
                prog[pos] = 1
            else:
                pos = getPosition(prog, ind, relBase)
                prog[pos] = 0
            ind += 4
        elif str(prog[ind])[-2:] == "09": # value 9 (complex 1, 2)
            if str(prog[ind])[-3] == "1":
                relBase += prog[ind + 1]
            else:
                relBase += prog[prog[ind + 1] + relBase]
            ind += 2

face = "U"
turnR = {"U":"R", "R":"D", "D":"L", "L":"U"}
turnL = {"U":"L", "L":"D", "D":"R", "R":"U"}
direct = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}
painted = set()
white = set()
black = set()

for x in range(-100, 100):
    for y in range(-100, 100):
        black.add((x, y))

test1 = prog.copy()
inp = [0]
out = []
x = 0
y = 0
ind = 0
relBase = 0
while True:
    test1, ind, relBase = runProgv5(test1, ind, relBase, inp, 0, out, True)
    if test1 == "Program finished":
        break
    test1, ind, relBase = runProgv5(test1, ind, relBase, inp, 0, out, True)
    if test1 == "Program finished":
        break
    if out[-2] == 0: # paint black
        painted.add((x, y))
        black.add((x, y))
        if (x, y) in white:
            white.remove((x, y))
    elif out[-2] == 1: # paint white
        painted.add((x, y))
        white.add((x, y))
        if (x, y) in black:
            black.remove((x, y))
    if out[-1] == 0:
        face = turnL[face]
    elif out[-1] == 1:
        face = turnR[face]
    x += direct[face][0]
    y += direct[face][1]
    if (x, y) in white:
        inp = [1]
    elif (x, y) in black:
        inp = [0]
print(len(painted))

face = "U"
turnR = {"U":"R", "R":"D", "D":"L", "L":"U"}
turnL = {"U":"L", "L":"D", "D":"R", "R":"U"}
direct = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}
painted = set()
white = set()
black = set()

for x in range(-100, 100):
    for y in range(-100, 100):
        black.add((x, y))

test2 = prog.copy()
inp = [1]
out = []
x = 0
y = 0
ind = 0
relBase = 0
while True:
    test2, ind, relBase = runProgv5(test2, ind, relBase, inp, 0, out, True)
    if test2 == "Program finished":
        break
    test2, ind, relBase = runProgv5(test2, ind, relBase, inp, 0, out, True)
    if test2 == "Program finished":
        break
    if out[-2] == 0: # paint black
        painted.add((x, y))
        black.add((x, y))
        if (x, y) in white:
            white.remove((x, y))
    elif out[-2] == 1: # paint white
        painted.add((x, y))
        white.add((x, y))
        if (x, y) in black:
            black.remove((x, y))
    if out[-1] == 0:
        face = turnL[face]
    elif out[-1] == 1:
        face = turnR[face]
    x += direct[face][0]
    y += direct[face][1]
    if (x, y) in white:
        inp = [1]
    elif (x, y) in black:
        inp = [0]
line1 = "" # y va de -5 a 0, x va de 1 a 39
line2 = ""
line3 = ""
line4 = ""
line5 = ""
line6 = ""
for x in range(1, 40):
    if (x, 0) in white:
        line1 = line1 + "#"
    else:
        line1 = line1 + " "
for x in range(1, 40):
    if (x, -1) in white:
        line2 = line2 + "#"
    else:
        line2 = line2 + " "
for x in range(1, 40):
    if (x, -2) in white:
        line3 = line3 + "#"
    else:
        line3 = line3 + " "
for x in range(1, 40):
    if (x, -3) in white:
        line4 = line4 + "#"
    else:
        line4 = line4 + " "
for x in range(1, 40):
    if (x, -4) in white:
        line5 = line5 + "#"
    else:
        line5 = line5 + " "
for x in range(1, 40):
    if (x, -5) in white:
        line6 = line6 + "#"
    else:
        line6 = line6 + " "
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)