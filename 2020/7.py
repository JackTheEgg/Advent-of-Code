bags = {}
with open("7.txt") as file:
    for line in file:
        info = line.strip().split(" bags contain ")
        contents = info[1].split(", ")
        if not info[0] in bags:
            bags[info[0]] = contents

for k, v in bags.items():
    if v[0] == "no other bags":
        bags[k] = 0
    else:
        d = {}
        for bag in v:
            params = bag.split(" ")
            d[params[1] + " " + params[2]] = int(params[0])
        bags[k] = d

goldenBags = []
for k, v in bags.items():
    if v != 0 and ("shiny gold" in v):
        goldenBags.append(k)

while True:
    check = len(goldenBags)
    for k, v in bags.items():
        if v != 0:
            for goldenBag in goldenBags:
                if goldenBag in v and not k in goldenBags:
                    goldenBags.append(k)
    if len(goldenBags) == check: 
        break
print(len(goldenBags))

bagsInGold = {}
for k, v in bags.items():
    if k == "shiny gold":
        for bag in v:
            if not bag in bagsInGold:
                bagsInGold[bag] = 0

while True:
    check = len(bagsInGold)
    for k, v in bags.items():
        if k in bagsInGold and v != 0:
            for bag in v:
                if not bag in bagsInGold:
                    bagsInGold[bag] = 0
        elif v == 0:
            if not k in bagsInGold:
                bagsInGold[k] = 0
    if check == len(bagsInGold):
        break

for bag, amount in bags["shiny gold"].items():
    if bag in bagsInGold:
        bagsInGold[bag] = bagsInGold[bag] + amount

for bag, total in bagsInGold.items():
    if bags[bag] == 0:
        continue
    else:    
        for bag, amount in bags[bag].items():
            bagsInGold[bag] = bagsInGold[bag] + total*(amount)

total = 0
for _, value in bagsInGold.items():
    total += value
print(total)