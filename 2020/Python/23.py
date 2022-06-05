cups = []
with open("23.txt") as f:
    for line in f:
        for digit in line.strip():
            cups.append(int(digit))
transf = {0:9, -1:8, -2:7, -3:6, -4:5}
ccupindex = 0
for n in range(1, 101):
    ccup = cups[ccupindex]
    cup1 = cups[(ccupindex + 1) % 9]
    cup2 = cups[(ccupindex + 2) % 9]
    cup3 = cups[(ccupindex + 3) % 9]
    ncup = cups[(ccupindex + 4) % 9]
    cups.remove(cup1)
    cups.remove(cup2)
    cups.remove(cup3)
    for i in range(1, 10):
        if ccup - i > 0:
            if ccup - i in cups:
                destCup = ccup - i
                destCupindex = cups.index(destCup)
                break
        elif ccup - i <= 0:
            if transf[ccup - i] in cups:
                destCup = transf[ccup - i]
                destCupindex = cups.index(destCup)
                break
    cups.insert((destCupindex + 1) % 9, cup3)
    cups.insert((destCupindex + 1) % 9, cup2)
    cups.insert((destCupindex + 1) % 9, cup1)
    ccupindex = cups.index(ncup)

in1 = cups.index(1)
num = ""
for i in range(in1 + 1, len(cups)):
    num = num + str(cups[i])
for i in range(in1):
    num = num + str(cups[i])
print(num)

cups = []
with open("23.txt") as f:
    for line in f:
        for digit in line.strip():
            cups.append(int(digit))

def solve_game(cups, full_len, num_moves):
    cuplist = {}
    for i in range(full_len):
        if i < len(cups) - 1:
            cuplist[cups[i]] = cups[i + 1]
        elif i == len(cups) - 1 and len(cups) == full_len:
            cuplist[cups[i]] = cups[0]
        elif i == len(cups) - 1 and len(cups) < full_len:
            cuplist[cups[i]] = max(cups) + 1
        elif i < full_len - 1:
            cuplist[i + 1] = i + 2
        elif i == full_len - 1:
            cuplist[i + 1] = cups[0]
    ptr = cups[0]
    for _ in range(num_moves):
        c1 = cuplist[ptr]
        c2 = cuplist[c1]
        c3 = cuplist[c2]
        cuplist[ptr] = cuplist[c3]
        dest = ((ptr - 2) % full_len) + 1
        while dest in [c1, c2, c3]:
            dest = ((dest - 2) % full_len) + 1
        cuplist[c3] = cuplist[dest]
        cuplist[dest] = c1
        ptr = cuplist[ptr]
    return cuplist

solved = solve_game(cups, 1000000, 10000000)
res = solved[1] * solved[solved[1]]
print(res)