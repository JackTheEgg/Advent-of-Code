from collections import defaultdict

class Intcode:
    def __init__(self, data, values = None):
        self.prog = defaultdict(int)
        for i, j in enumerate(map(int, data.split(","))):
            self.prog[i] = j
        if values is None:
            self.values = []
        else:
            self.values = values
        self.pos = 0
        self.rel_base = 0
        self.output = None

    def set(self, i, v, mode):
        if mode == "0":
            self.prog[self.prog[self.pos+i]] = v
        else:
            self.prog[self.prog[self.pos+i] + self.rel_base] = v

    def get(self, i, mode):
        if mode == "0":
            return self.prog[self.prog[self.pos+i]]
        elif mode == "1":
            return self.prog[self.pos+i]
        elif mode == "2":
            return self.prog[self.prog[self.pos+i]+self.rel_base]

    def run(self):
        while True:
            instruction = str(self.prog[self.pos]).zfill(5)
            opcode = instruction[3:]
            modes = list(reversed(instruction[:3]))
            a, b = None, None
            try:
                a = self.get(1, modes[0])
                b = self.get(2, modes[1])
            except IndexError:
                pass
            if opcode == "01":
                self.set(3, a + b, modes[2])
                self.pos += 4
            elif opcode == "02":
                self.set(3, a * b, modes[2])
                self.pos += 4
            elif opcode == "03":
                if len(self.values) == 0:
                    yield None
                self.set(1, self.values.pop(0), modes[0])
                self.pos += 2
            elif opcode == "04":
                yield self.get(1, modes[0])
                self.output = self.get(1, modes[0])
                self.pos += 2
            elif opcode == "05":
                self.pos = b if a != 0 else self.pos+3
            elif opcode == "06":
                self.pos = b if a == 0 else self.pos+3
            elif opcode == "07":
                self.set(3, 1 if a < b else 0, modes[2])
                self.pos += 4
            elif opcode == "08":
                self.set(3, 1 if a == b else 0, modes[2])
                self.pos += 4
            elif opcode == "09":
                self.rel_base += a
                self.pos += 2
            else:
                assert opcode == "99"
                return self.output

def printASCII(out):
    print("".join(list(map(chr, list(out)[:-1]))))

prog = Intcode(open("17.txt").read())
prog.prog[0] = 2

print("=== Define the main routines ===")
main = input()
while len(main) > 20:
    print("That routine is too long")
    main = input()
main = list(map(ord, list(main))) + [10]
prog.values += main
print("=== Define function A ===")
Afunc = input()
while len(Afunc) > 20:
    print("That function is too long")
    Afunc = input()
Afunc = list(map(ord, list(Afunc))) + [10]
prog.values += Afunc
print("=== Define function B ===")
Bfunc = input()
while len(Bfunc) > 20:
    print("That function is too long")
    Bfunc = input()
Bfunc = list(map(ord, list(Bfunc))) + [10]
prog.values += Bfunc
print("=== Define function C ===")
Cfunc = input()
while len(Cfunc) > 20:
    print("That function is too long")
    Cfunc = input()
Cfunc = list(map(ord, list(Cfunc))) + [10]
prog.values += Cfunc
print("Enable video feed? y/n")
video = list(map(ord, list(input()))) + [10]
prog.values += video
out = prog.run()
printASCII(out)

#1415975
# ord para pasar de letra a ASCII, chr para pasar de ASCII a letra
# A,B,A,A,B,C,B,C,C,B
# L,12,R,8,L,6,R,8,L,6
# R,8,L,12,L,12,R,8
# L,6,R,6,L,12