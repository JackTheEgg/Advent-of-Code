import time
import random

with open("15.txt") as f:
    for line in f:
        prog = list(map(int, line.strip().split(",")))
for i in range(10000):
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
            return "Program finished", ind, prog
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
#prog, ind, relBase = runProgv5(prog, ind, relBase, inp, inpInd, out, useLoop = True)

'''
Only four movement commands are understood: north (1), south (2), west (3), and east (4)

0: The repair droid hit a wall. Its position has not changed.
1: The repair droid has moved one step in the requested direction.
2: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.
'''

movs = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
walls, visited, x, y, oxygen, start = set(), set(), 0, 0, "", (0,0)
visited.add(start)
ind, relBase = 0, 0

for n in range(10000000):
    print(n)
    inp, out = [random.randint(1,4)], []
    prog, ind, relBase = runProgv5(prog, ind, relBase, inp, 0, out, True)
    if out == [0]:
        walls.add((x + movs[inp[0]][0], y + movs[inp[0]][1]))
    elif out == [1]:
        x += movs[inp[0]][0]
        y += movs[inp[0]][1]
        visited.add((x, y))
    elif out == [2]:
        x += movs[inp[0]][0]
        y += movs[inp[0]][1]
        oxygen = (x, y)
    '''
    for y in range(21, -20, -1): # y va de 21 a -19
        line = ""
        for x in range(-21, 20): # x va de -21 a 19
            if (x, y) == start:
                line = line + "S"
            elif (x, y) == oxygen:
                line = line + "O"
            elif (x, y) in visited:
                line = line + " "
            elif (x, y) in walls:
                line = line + "#"
            else:
                line = line + "·"
        print(line)
    '''
for y in range(21, -20, -1): 
    line = ""
    for x in range(-21, 20):
        if (x, y) == start:
            line = line + "S"
        elif (x, y) == oxygen:
            line = line + "O"
        elif (x, y) in visited:
            line = line + " "
        elif (x, y) in walls:
            line = line + "#"
        else:
            line = line + "·"
    print(line)
