import copy

commands = []
with open("8.txt") as file:
    for line in file:
        command = line.strip().split(" ")
        command[1] = int(command[1])
        command.append(False)
        commands.append(command)

def runCode(commands, step, accumulator):
    while True:
        if step > len(commands) - 1:
            print("Program successful. Accumulator value:", accumulator)
            return True
        elif commands[step][0] == "nop" and not commands[step][2]:
            commands[step][2] = True
            step += 1
        elif commands[step][0] == "acc" and not commands[step][2]:
            accumulator += commands[step][1]
            commands[step][2] = True
            step += 1
        elif commands[step][0] == "jmp" and not commands[step][2]:
            commands[step][2] = True
            step += commands[step][1]
        else:
            print("Program failed. Accumulator value:", accumulator)
            return False
commandsCopy = copy.deepcopy(commands)
print("---PART1---")
runCode(commands, 0, 0)
print("---PART2---")
result = None
for i in range(len(commandsCopy)):
    if result:
        break
    newTry = copy.deepcopy(commandsCopy)
    if newTry[i][0] == "nop":
        newTry[i][0] = "jmp"
        result = runCode(newTry, 0, 0)
    elif newTry[i][0] == "jmp":
        newTry[i][0] = "nop"
        result = runCode(newTry, 0, 0)