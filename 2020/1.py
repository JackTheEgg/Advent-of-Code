values = []

with open("1.txt") as file:
    for line in file:
        values.append(int(line))

stopLooping = False
for i in range(len(values)):
    if stopLooping:
        break
    for value in values:
        if value + values[i] == 2020:
            print(value*values[i])
            stopLooping = True
            break

stopLooping = False
for i in range(len(values)):
    if stopLooping:
        break
    for j in range(len(values)):
        if stopLooping:
            break
        for value in values:
            if value + values[i] + values[j] == 2020:
                print(value*values[i]*values[j])
                stopLooping = True
                break