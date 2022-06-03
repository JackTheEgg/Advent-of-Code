passes = []
with open("5.txt") as file:
    for line in file:
        line.strip()
        passes.append(line)

def getScore(s):
    rows = []
    cols = []
    for i in range(128):
        rows.append(i)
    for i in range(8):
        cols.append(i)
    for letter in s:
        midrow = len(rows) // 2
        midcol = len(cols) // 2
        if letter == "F":
            del rows[midrow:]
        elif letter == "B":
            del rows[:midrow]
        elif letter == "R":
            del cols[:midcol]
        elif letter == "L":
            del cols[midcol:]
    row = rows[0]
    col = cols[0]
    return row*8 + col

scores = []
for ticket in passes:
    score = getScore(ticket)
    scores.append(score)
scores.sort()
print(scores[-1])

for score in scores:
    if not score + 1 in scores:
        print("Your ticket score is", score + 1)
        break