orbits = {}
with open("6.txt") as f:
    for line in f:
        orbit = line.strip().split(")")
        orbits[orbit[1]] = [orbit[0]]

while True:
    movCount = 0
    for k, v in orbits.items():
        if v[0] in orbits:
            for planet in orbits[v[0]]:
                if not planet in v:
                    v.append(planet)
                    movCount += 1
    if movCount == 0:
        break 

count = 0 
for k, v in orbits.items():
    count += len(v)
print(count)

SANtoCOM = []
YOUtoCOM = []
nex = "SAN"
while True:
    SANtoCOM.append(orbits[nex][0])
    if orbits[nex][0] == "COM":
        break
    else:
        nex = orbits[nex][0]
nex = "YOU"
while True:
    YOUtoCOM.append(orbits[nex][0])
    if orbits[nex][0] == "COM":
        break
    else:
        nex = orbits[nex][0]

for station in SANtoCOM:
    if station in YOUtoCOM:
        point = station
        break

SANpoint = SANtoCOM.index(point)
YOUpoint = YOUtoCOM.index(point)
SANtoCOM = SANtoCOM[:SANpoint]
YOUtoCOM = YOUtoCOM[:YOUpoint]
print(len(SANtoCOM) + len(YOUtoCOM))