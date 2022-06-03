count = 0
with open("1.txt") as f:
    for line in f:
        count += (int(line.strip()) // 3) - 2
print(count)

count = 0
with open("1.txt") as f:
    for line in f:
        fuel = []
        fuel.append((int(line.strip()) // 3) - 2)
        while True:
            newFuel = (fuel[-1] // 3) - 2
            if newFuel > 0:
                fuel.append(newFuel)
            else:
                break
        for digit in fuel:
            count += digit
print(count)