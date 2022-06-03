import re

file = open("16.txt").readlines()

params = []
for i in range(20): # get the fields (input is 20, example is 3)
    params.append(file[i].strip().split(": "))

ranges = {}
for i in range(len(params)):
    ranges[params[i][0]] = list(map(int, re.split("\D+", params[i][1])))

myTicket = list(map(int, file[22].strip().split(","))) #get my ticket (input is 22, example is 5)

otherTickets = []
for i in range(25, 260): #get the other tickets (input is 25 - 260, example is 8 - 12(1)/11(2))
    otherTickets.append(list(map(int, file[i].strip().split(","))))

badParams = []
for ticket in otherTickets:
    for value in ticket:
        for _, v in ranges.items():
            if (v[0] <= value <= v[1]) or (v[2] <= value <= v[3]):
                isBad = False
                break
            isBad = True
        if isBad:
            badParams.append(value)

count = 0
for num in badParams:
    count += num
print(count)

badIndexes = []
for i, table in enumerate(otherTickets): # remove the bad tickets from the list
    for param in table:
        if param in badParams:
            badIndexes.append(i)
            break
badIndexes = sorted(badIndexes, reverse = True)
for index in badIndexes:
    del otherTickets[index]
otherTickets.append(myTicket)

validIDs = {}
for k, v in ranges.items():
    IDs = []
    for i in range(len(myTicket)):
        isValid = True
        for j in range(len(otherTickets)):
            if not ((v[0] <= otherTickets[j][i] <= v[1]) or (v[2] <= otherTickets[j][i] <= v[3])):
                isValid = False
                break
        if isValid:
            IDs.append(i)
    validIDs[k] = IDs

defIDs = {}
for k in validIDs.keys():
    defIDs[k] = 0

assignedIDs = 0
while assignedIDs < len(validIDs):
    for k, v in validIDs.items():
        if len(v) == 1:
            defIDs[k] = v[0]
            needsRemove = v[0]
            assignedIDs += 1
            break
    for _, v in validIDs.items():
        if needsRemove in v:
            v.remove(needsRemove)

product = 1
for k in defIDs.keys():
    if k[:9] == "departure":
        product *= myTicket[defIDs[k]]
print(product)