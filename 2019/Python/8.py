width = 25
height = 6
layers = []
with open("8.txt") as f:
    for line in f:
        inp = line.strip()

cuts = round(len(inp) / (width * height))
ind = 0
for i in range(cuts):
    layer = []
    for i in range(round(width * height)):
        layer.append(int(inp[ind]))
        ind += 1
    layers.append(layer)

zeroCount = list(layers[i].count(0) for i in range(len(layers)))
targetind = zeroCount.index(min(zeroCount))
print(layers[targetind].count(1) * layers[targetind].count(2))

def processImage(lst):
    finalImg = ""
    for i in range(len(lst[0])):
        seen = "2"
        for j in range(len(lst) - 1, -1, -1):
            if lst[j][i] == 2:
                continue
            elif lst[j][i] == 1:
                seen = "#"
            elif lst[j][i] == 0:
                seen = " "
        finalImg = finalImg + seen
    return finalImg

img = processImage(layers)
print(img[0:24])
print(img[25:49])
print(img[50:74])
print(img[75:99])
print(img[100:124])
print(img[125:149])