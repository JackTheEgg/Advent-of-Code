import re
import random
import copy

def getMask(s):
    mask = []
    for char in s[7:]:
        mask.append(char)
    return mask

def getParams(s):
    params = re.split("\D+", s)
    return int(params[1]), int(params[2])

def decToBin(num):
    binary = []
    binNum = bin(int(num))
    for char in binNum[2:]:
        binary.append(char)
    while len(binary) < 36:
        binary.insert(0, "0")
    return binary

def applyMask(number, mask):
    for i in range(len(mask)):
        if mask[i] == "0":
            number[i] = "0"
        elif mask[i] == "1":
            number[i] = "1"
    return number

def binToDec(num):
    dec = ""
    for char in num:
        dec = dec + char
    return int(dec, 2)

mem = {}
with open("14.txt") as file:
    for line in file:
        if line[0:4] == "mask":
            mask = getMask(line.strip())
        else:
            index, value = getParams(line.strip())
            binNum = decToBin(value)
            newNum = applyMask(binNum, mask)
            decNum = binToDec(newNum)
            mem[index] = decNum

count = 0
for k, v in mem.items():
    count += v
print(count)

def applyMaskv2(number, mask):
    for i in range(len(mask)):
        if mask[i] == "X":
            number[i] = "X"
        elif mask[i] == "1":
            number[i] = "1"
    return number

comb = {0:1}
for i in range(1, 37):
    comb[i] = comb[i-1] * 2

def genIndexes(baseIndex):
    xcount = 0
    for index in baseIndex:
        if index == "X":
            xcount += 1
    maxCombs = comb[xcount]
    indexes = []
    while len(indexes) < maxCombs:
        testIndex = copy.deepcopy(baseIndex)
        for i in range(len(baseIndex)):
            if testIndex[i] == "X":
                testIndex[i] = str(random.randrange(0,2))
        newIndex = binToDec(testIndex)
        if not newIndex in indexes:
            indexes.append(newIndex)
    return indexes

mem = {}
with open("14.txt") as file:
    for line in file:
        if line[0:4] == "mask":
            mask = getMask(line.strip())
        else:
            index, value = getParams(line.strip())
            binIndex = decToBin(index)
            newIndex = applyMaskv2(binIndex, mask)
            indexes = genIndexes(newIndex)
            for number in indexes:
                mem[number] = value

count = 0
for k, v in mem.items():
    count += v
print(count)