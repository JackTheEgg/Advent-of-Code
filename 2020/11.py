import copy

seats = []
with open("11.txt") as file:
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        seats.append(row)
seatsCopy = copy.deepcopy(seats)

for n in range(1, 1000):
    movCount = 0
    for i in range(1, len(seats) - 1):
        for j in range(1, len(seats[0]) - 1):
            if seats[i][j] == "L":
                count = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if k == l == 0:
                            continue
                        if seats[i+k][j+l] == "#":
                            count += 1
                if count == 0:
                    seatsCopy[i][j] = "#"
                    movCount += 1
            elif seats[i][j] == "#":
                count = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if k == l == 0:
                            continue
                        if seats[i+k][j+l] == "#":
                            count += 1
                if count >= 4:
                    seatsCopy[i][j] = "L"
                    movCount += 1
    seats = copy.deepcopy(seatsCopy)
    if movCount == 0:
        break

occupied = 0
for rows in seats:
    for row in rows:
        for place in row:
            if place == "#":
                occupied += 1
print(occupied)

directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
def checkDirections(list, index1, index2):
    countOccupied = 0
    for direction in directions:
        y = index1
        x = index2
        while (0 < y < len(list) - 1) and (0 < x < len(list[0]) - 1):
            if list[y+direction[0]][x+direction[1]] == "L":
                break
            elif list[y+direction[0]][x+direction[1]] == "#":
                countOccupied += 1
                break
            else:
                y += direction[0]
                x += direction[1]       
    return countOccupied

seats = []
with open("11.txt") as file:
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        seats.append(row)
seatsCopy = copy.deepcopy(seats)

for n in range(1, 1000):
    movCount = 0
    for i in range(1, len(seats) - 1):
        for j in range(1, len(seats[0]) - 1):
            if seats[i][j] == "L":
                count = checkDirections(seats, i, j)
                if count == 0:
                    seatsCopy[i][j] = "#"
                    movCount += 1
            elif seats[i][j] == "#":
                count = checkDirections(seats, i, j)
                if count >= 5:
                    seatsCopy[i][j] = "L"
                    movCount += 1
    seats = copy.deepcopy(seatsCopy)
    if movCount == 0:
        break

occupied = 0
for rows in seats:
    for row in rows:
        for place in row:
            if place == "#":
                occupied += 1
print(occupied)