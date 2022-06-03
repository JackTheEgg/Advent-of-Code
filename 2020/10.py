adapters = [0]
with open("10.txt") as file:
    for line in file:
        adapters.append(int(line.strip()))

adapters.sort()
adapters.append(adapters[-1] + 3)
differences = {"1": 0, "3": 0}
for i in range(len(adapters) - 1):
    if abs(adapters[i] - adapters[i+1]) == 1:
        differences["1"] += 1
    elif abs(adapters[i] - adapters[i+1]) == 3:
        differences["3"] += 1
print(differences["1"]*differences["3"])

paths = {}
for i in range(-1, adapters[-1] + 1):
    paths[i] = 0
paths[0] = 1
paths[1] = 1

for i in range(2, len(adapters)):
    paths[adapters[i]] = paths[adapters[i] - 1] + paths[adapters[i] - 2] + paths[adapters[i] - 3]
print(paths[adapters[-1]])