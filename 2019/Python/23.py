import sys
from collections import deque, defaultdict


class IntCode(object):
    """ IntCode virtual machine """
    grid = defaultdict(str)

    def __init__(self, name, code, inp):
        self.name = name
        self.program_param = {}
        self.pos = 0
        self.output = 0
        self.program = {}
        self.io = deque()
        self.io.append(inp)
        self.relative_base = 0
        self.x = 50
        self.y = 50
        self.__direction = '^'

        i = 0
        for instr in code:
            self.program[i] = instr
            i += 1

    def __str__(self):
        return 1

    def get_input(self):
        """
        Gets input for the IntCode VM
        :param self.cur_proc: Which processor is now running
        (to enable multiple codes running at the same time)
        :return: the value of input
        """

#        print("Processor ",self.name," getting input")
        if len(self.io) > 0:
            instr = self.io.popleft()
        else:
            instr = -1
        return int(instr)

    def process_output(self):
        # if we have seen all address,
        # x, y, return it and delete from the queue
        if len(self.io) == 3:
            addr = self.io.popleft()
            x = self.io.popleft()
            y = self.io.popleft()
            return(addr, x, y)

        # otherwise keep running
        return (-1, -1, -1)

    def run_intcode(self):
        params = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}

        while 1:
            instr = self.program[self.pos]

            op = instr % 100

            mode1 = int(instr / 100) % 10
            mode2 = int(instr / 1000) % 10
            mode3 = int(instr / 10000) % 10

            reg1 = self.program.get(self.pos + 1, 0)
            reg2 = self.program.get(self.pos + 2, 0)
            reg3 = self.program.get(self.pos + 3, 0)

            v1 = reg1

            if op != 3:
                if mode1 == 0:
                    v1 = self.program.get(reg1, 0)
                if mode1 == 2:
                    v1 = self.program.get(
                            reg1 + self.relative_base, 0)
            else:
                if mode1 == 2:
                    v1 += self.relative_base

            v2 = reg2
            if mode2 == 0:
                v2 = self.program.get(reg2, 0)
            if mode2 == 2:
                v2 = self.program.get(
                        reg2 + self.relative_base, 0)

            v3 = reg3
            if mode3 == 2:
                v3 += self.relative_base

            if op == 1:
                self.program[v3] = v1 + v2

            # Process the opcodes
            elif op == 2:
                self.program[v3] = v1 * v2

            elif op == 3:
                self.program[v1] = self.get_input()
                if self.program[v1] == -1:
                    self.pos += 2
                    return(-1, -1, -1)

            elif op == 4:
                self.io.append(v1)
                (addr, x, y) = self.process_output()
                if addr != -1:
                    self.pos += 2
                    return (addr, x, y)

            elif (op == 5):
                if v1 > 0:
                    self.pos = v2
                    continue

            elif op == 6:
                if v1 == 0:
                    self.pos = v2
                    continue

            elif op == 7:
                if int(v1) < int(v2):
                    self.program[v3] = 1
                else:
                    self.program[v3] = 0

            elif op == 8:
                if v1 == v2:
                    self.program[v3] = 1
                else:
                    self.program[v3] = 0

            elif op == 9:
                self.relative_base += v1

            elif op == 99:
                return self.io

            else:
                sys.exit("Unknown argument found")

            shift = params[op] + 1
            self.pos = self.pos + shift

def is_network_idle():
    for i in range(50):
        if len(processors[i].io) > 0:
            return 0
    return 1


data = list(map(int, open("23.txt").read().strip().split(',')))

processors = deque()

for i in range(50):
    processor = IntCode(i, data, i)
    processors.append(processor)

i = 0
addr = 0

natx = naty = None
prev_naty = None
part = 1
empty_count = 0

while 1:
    (addr, x, y) = processors[i].run_intcode()

    if addr != -1 and addr != 255:
        processors[addr].io.append(x)
        processors[addr].io.append(y)
        empty_count = 0
        i = addr

    elif addr == 255:
        if part == 1:
            print(y)
            part += 1

        natx = x
        naty = y
        empty_count = 0

    else:
        if is_network_idle() == 1:
            if empty_count == 10000:
                if prev_naty and naty == prev_naty:
                    print(naty)
                    break

                prev_naty = naty

                processors[0].io.append(natx)
                processors[0].io.append(naty)
                empty_count = 0
            else:
                empty_count += 1
        i += 1
        i %= 50