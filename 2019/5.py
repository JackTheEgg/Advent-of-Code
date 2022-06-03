with open("5.txt") as f:
    for line in f:
        prog = list(map(int, line.strip().split(",")))

progCopy = prog.copy()

def runProgv2(prog, ind, inp):
    while True:
        if prog[ind] == 99:
            return
        elif prog[ind] == 3:
            prog[prog[ind + 1]] = inp
            ind += 2
        elif prog[ind] == 4:
            print(prog[prog[ind + 1]])
            ind += 2
        elif prog[ind] == 1:
            prog[prog[ind + 3]] = prog[prog[ind + 2]] + prog[prog[ind + 1]]
            ind += 4
        elif prog[ind] == 2:
            prog[prog[ind + 3]] = prog[prog[ind + 2]] * prog[prog[ind + 1]]
            ind += 4
        elif str(prog[ind])[-2:] == "01" and len(str(prog[ind])) >= 4:
            value1 = (str(prog[ind])[-3] == "1" and prog[ind + 1]) or prog[prog[ind + 1]]
            value2 = (str(prog[ind])[-4] == "1" and prog[ind + 2]) or prog[prog[ind + 2]]
            prog[prog[ind + 3]] = value1 + value2 
            ind += 4
        elif str(prog[ind])[-2:] == "01" and len(str(prog[ind])) == 3:
            value1 = (str(prog[ind])[-3] == "1" and prog[ind + 1]) or prog[prog[ind + 1]]
            value2 = prog[prog[ind + 2]]
            prog[prog[ind + 3]] = value1 + value2 
            ind += 4
        elif str(prog[ind])[-2:] == "02" and len(str(prog[ind])) >= 4:
            value1 = (str(prog[ind])[-3] == "1" and prog[ind + 1]) or prog[prog[ind + 1]]
            value2 = (str(prog[ind])[-4] == "1" and prog[ind + 2]) or prog[prog[ind + 2]]
            prog[prog[ind + 3]] = value1 * value2 
            ind += 4
        elif str(prog[ind])[-2:] == "02" and len(str(prog[ind])) == 3:
            value1 = (str(prog[ind])[-3] == "1" and prog[ind + 1]) or prog[prog[ind + 1]]
            value2 = prog[prog[ind + 2]]
            prog[prog[ind + 3]] = value1 * value2 
            ind += 4
        elif str(prog[ind])[-2:] == "04":
            if str(prog[ind])[-3] == "1":
                print(prog[ind + 1])
            else:
                print(prog[prog[ind + 1]])
            ind += 2
runProgv2(prog, 0, 1)

def runProgv3(prog, ind, inp):
    while True:
        if prog[ind] == 99: # value 99
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
        elif prog[ind] == 3: # value 3 (simple)
            prog[prog[ind + 1]] = inp
            ind += 2
        elif prog[ind] == 4: # value 4 (simple)
            print(prog[prog[ind + 1]])
            ind += 2
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
                print(prog[ind + 1])
            else:
                print(prog[prog[ind + 1]])
            ind += 2
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
runProgv3(progCopy, 0, 5)