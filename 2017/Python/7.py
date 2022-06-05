import sys

progN = {}
progs = {}
tWeight = {}
with open("7.txt") as f:
    for line in f:
        inp = line.strip().split()
        if len(inp) == 2:
            progs[inp[0]] = []
            progN[inp[0]] = int(inp[1][1:-1])
            tWeight[inp[0]] = int(inp[1][1:-1])
        else:
            progs[inp[0]] = inp[3:]
            progN[inp[0]] = int(inp[1][1:-1])

def buildLayers(start):
    progL = {1:set()}
    progL[1].add(start)
    layer = 1
    while True:
        movCount = 0
        for item in progL[layer]:
            if len(progs[item]) > 0:
                if not layer + 1 in progL:
                    progL[layer + 1] = set()
                    for prog in progs[item]:
                        progL[layer + 1].add(prog)
                    movCount += 1
                else:
                    for prog in progs[item]:
                        progL[layer + 1].add(prog)
                    movCount += 1       
        if movCount == 0:
            return progL
        layer += 1

for prog, conts in progs.items():
    if len(conts) != 0:
        layers = buildLayers(prog)
        if sum(len(item) for item in layers.values()) == len(progN):
            break
print(layers[1])

for i in range(len(layers) - 1, 0, -1):
    for item in layers[i]:
        if len(progs[item]) != 0:
            weights = {}
            for p in progs[item]:
                weights[p] = tWeight[p]
            if len(set(weights.values())) != 1: # unbalanced
                vals = list(weights.values())
                vals.sort()
                if vals[0] != vals[1]: # lighter than the rest
                    for k, v in weights.items():
                        if v == vals[0]:
                            print(progN[k] + (vals[1] - vals[0]))
                            sys.exit()
                else: # heavier than the rest
                    for k, v in weights.items():
                        if v == vals[-1]:
                            print(progN[k] - (vals[-1] - vals[-2]))
                            sys.exit()
            else:
                tWeight[item] = sum(weights.values()) + progN[item]