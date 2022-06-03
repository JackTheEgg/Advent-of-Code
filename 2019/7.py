import itertools

with open("7.txt") as f:
    for line in f:
        prog = list(map(int, line.strip().split(",")))

def runProgv4(prog, ind, inp, inpInd, out, useLoop = False):
    while True:
        if prog[ind] == 99: # value 99
            return "Program finished", ind, inpInd
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
        elif prog[ind] == 3: # value 3 (simple)
            prog[prog[ind + 1]] = inp[inpInd]
            ind += 2
            inpInd += 1
        elif prog[ind] == 4: # value 4 (simple)
            output = prog[prog[ind + 1]]
            ind += 2
            out.append(output)
            if useLoop:
                return prog, ind, inpInd
            else:
                return
        elif prog[ind] == 1: # value 1 (simple)
            prog[prog[ind + 3]] = prog[prog[ind + 2]] + prog[prog[ind + 1]]
            ind += 4
        elif prog[ind] == 2: # value 2 (simple)
            prog[prog[ind + 3]] = prog[prog[ind + 2]] * prog[prog[ind + 1]]
            ind += 4
        elif str(prog[ind])[-2:] == "01": # value 1 (complex)
            if str(prog[ind])[-3] == "1":
                value1 = prog[ind + 1]
            else:
                value1 = prog[prog[ind + 1]]
            if len(str(prog[ind])) >= 4:    
                if str(prog[ind])[-4] == "1":
                    value2 = prog[ind + 2]
                else:
                    value2 = prog[prog[ind + 2]]
            elif len(str(prog[ind])) == 3:
                value2 = prog[prog[ind + 2]]
            prog[prog[ind + 3]] = value1 + value2 
            ind += 4
        elif str(prog[ind])[-2:] == "02": # value 2 (complex)
            if str(prog[ind])[-3] == "1":
                value1 = prog[ind + 1]
            else:
                value1 = prog[prog[ind + 1]]
            if len(str(prog[ind])) >= 4:    
                if str(prog[ind])[-4] == "1":
                    value2 = prog[ind + 2]
                else:
                    value2 = prog[prog[ind + 2]]
            elif len(str(prog[ind])) == 3:
                value2 = prog[prog[ind + 2]]
            prog[prog[ind + 3]] = value1 * value2 
            ind += 4
        elif str(prog[ind])[-2:] == "04": # value 4 (complex)
            if str(prog[ind])[-3] == "1":
                output = prog[ind + 1]
            else:
                output = prog[prog[ind + 1]]
            ind += 2
            out.append(output)
            if useLoop:
                return prog, ind, inpInd
            else:
                return
        elif str(prog[ind])[-2:] == "05": # value 5 (complex)
            if str(prog[ind])[-3] == "1":
                value1 = prog[ind + 1]
            else:
                value1 = prog[prog[ind + 1]]
            if len(str(prog[ind])) >= 4:    
                if str(prog[ind])[-4] == "1":
                    value2 = prog[ind + 2]
                else:
                    value2 = prog[prog[ind + 2]]
            elif len(str(prog[ind])) == 3:
                value2 = prog[prog[ind + 2]]
            if value1 != 0:
                ind = value2
            else:
                ind += 3
        elif str(prog[ind])[-2:] == "06": # value 6 (complex)
            if str(prog[ind])[-3] == "1":
                value1 = prog[ind + 1]
            else:
                value1 = prog[prog[ind + 1]]
            if len(str(prog[ind])) >= 4:    
                if str(prog[ind])[-4] == "1":
                    value2 = prog[ind + 2]
                else:
                    value2 = prog[prog[ind + 2]]
            elif len(str(prog[ind])) == 3:
                value2 = prog[prog[ind + 2]]
            if value1 == 0:
                ind = value2
            else:
                ind += 3
        elif str(prog[ind])[-2:] == "07": # value 7 (complex)
            if str(prog[ind])[-3] == "1":
                value1 = prog[ind + 1]
            else:
                value1 = prog[prog[ind + 1]]
            if len(str(prog[ind])) >= 4:    
                if str(prog[ind])[-4] == "1":
                    value2 = prog[ind + 2]
                else:
                    value2 = prog[prog[ind + 2]]
            elif len(str(prog[ind])) == 3:
                value2 = prog[prog[ind + 2]]
            if value1 < value2:
                prog[prog[ind + 3]] = 1
            else:
                prog[prog[ind + 3]] = 0
            ind += 4
        elif str(prog[ind])[-2:] == "08": # value 8 (complex)
            if str(prog[ind])[-3] == "1":
                value1 = prog[ind + 1]
            else:
                value1 = prog[prog[ind + 1]]
            if len(str(prog[ind])) >= 4:    
                if str(prog[ind])[-4] == "1":
                    value2 = prog[ind + 2]
                else:
                    value2 = prog[prog[ind + 2]]
            elif len(str(prog[ind])) == 3:
                value2 = prog[prog[ind + 2]]
            if value1 == value2:
                prog[prog[ind + 3]] = 1
            else:
                prog[prog[ind + 3]] = 0
            ind += 4

ways = list(itertools.permutations([0, 1, 2, 3, 4]))
outputs = []
for way in ways:
    inp = {"A": [way[0], 0], "B": [way[1]], "C": [way[2]], "D": [way[3]], "E": [way[4]]}
    runProgv4(prog, 0, inp["A"], 0, inp["B"])
    runProgv4(prog, 0, inp["B"], 0, inp["C"])
    runProgv4(prog, 0, inp["C"], 0, inp["D"])
    runProgv4(prog, 0, inp["D"], 0, inp["E"])
    runProgv4(prog, 0, inp["E"], 0, inp["A"])
    outputs.append(inp["A"][-1])
outputs.sort()
print(outputs[-1])

ways = list(itertools.permutations([5, 6, 7, 8, 9]))
outputs = []
for way in ways:
    inp = {"A": [way[0], 0], "B": [way[1]], "C": [way[2]], "D": [way[3]], "E": [way[4]]}
    progA, indA, inpA = prog.copy(), 0, 0
    progB, indB, inpB = prog.copy(), 0, 0
    progC, indC, inpC = prog.copy(), 0, 0
    progD, indD, inpD = prog.copy(), 0, 0
    progE, indE, inpE = prog.copy(), 0, 0
    while True:
        progA, indA, inpA = runProgv4(progA, indA, inp["A"], inpA, inp["B"], True)
        progB, indB, inpB = runProgv4(progB, indB, inp["B"], inpB, inp["C"], True)
        progC, indC, inpC = runProgv4(progC, indC, inp["C"], inpC, inp["D"], True)
        progD, indD, inpD = runProgv4(progD, indD, inp["D"], inpD, inp["E"], True)
        progE, indE, inpE = runProgv4(progE, indE, inp["E"], inpE, inp["A"], True)
        if progE == "Program finished":
            outputs.append(inp["A"][-1])
            break
outputs.sort()
print(outputs[-1])