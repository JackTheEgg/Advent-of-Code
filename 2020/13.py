waitTime = 0
buses = []
lineCount = 0
with open("13.txt") as file:
    for line in file:
        lineCount += 1
        if lineCount == 1:
            waitTime = int(line.strip())
        else:
            buses = line.strip().split(",")

depTimes = {}
times = []
for bus in buses:
    if bus.isnumeric():
        time = int(bus)
        for i in range(10000):
            if time * i >= waitTime:
                times.append(time * i)
                depTimes[int(bus)] = time * i
                break

times.sort()
goodBus = 0
for bus in depTimes.keys():
    if depTimes[bus] == times[0]:
        goodBus = bus
        break
print(goodBus*(times[0] - waitTime))

offsets = {}
for i in range(len(buses)):
    if buses[i].isnumeric():
        offsets[int(buses[i])] = -i % int(buses[i])

iterator = 0
increment = 1
for bus in offsets.keys():
    while iterator % bus != offsets[bus]:
        iterator += increment
    increment *= bus
print(iterator)