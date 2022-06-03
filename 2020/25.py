cardKey = 0
doorKey = 0
lineCount = 0
with open("25.txt") as f:
    for line in f:
        lineCount += 1
        if lineCount == 1:
            cardKey = int(line.strip())
        elif lineCount == 2:
            doorKey = int(line.strip())
cardLoop = 1
doorLoop = 1
while pow(7, cardLoop, 20201227) != cardKey:
    cardLoop += 1
while pow(7, doorLoop, 20201227) != doorKey:
    doorLoop += 1

encrKey = pow(cardKey, doorLoop, 20201227)
print(encrKey)