import random

with open("2.txt") as f:
    for line in f:
        program = list(map(int, line.strip().split(",")))
testProgram = program.copy()

program[1] = 12
program[2] = 2
def runProgram(program):
    for i in range(0, len(program), 4):
        if program[i] == 99:
            return program
        elif program[i] == 1:
            digit1 = program[program[i+1]]
            digit2 = program[program[i+2]]
            program[program[i+3]] = digit1 + digit2
        elif program[i] == 2:
            digit1 = program[program[i+1]]
            digit2 = program[program[i+2]]
            program[program[i+3]] = digit1 * digit2
    return program
runProgram(program)
print(program[0])

while True:
    attempt = testProgram.copy()
    digit1 = random.randint(0,99) # LOL
    digit2 = random.randint(0,99)
    attempt[1] = digit1
    attempt[2] = digit2
    runProgram(attempt)
    if attempt[0] == 19690720:
        print(100 * digit1 + digit2)
        break