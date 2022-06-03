trees = []
with open("3.txt") as file:
    for line in file:
        trees.append(line.strip()*10000)

down = 1
right = 3
count = 0

while True:
    if trees[down][right] == "#":
        count += 1
    if down == len(trees) - 1:
        break
    down += 1
    right += 3
print(count)

slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]] #down, right
treeCount = []
for slope in slopes:
    count = 0
    down = slope[0]
    right = slope[1]
    while True:
        if trees[down][right] == "#":
            count += 1
        if down == len(trees) - 1:
            treeCount.append(count)
            break
        down += slope[0]
        right += slope[1]

count = 1
for trees in treeCount:
    count = count * trees
print(count)