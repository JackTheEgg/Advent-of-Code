import re

inp = open("25.txt").read().strip()
info = list(map(int, re.findall("-?[0-9]+", inp))) # row, column

def get_code(row, col):
    triangle = (row + col-1) * (row + col) / 2
    return triangle - row + 1

n_iterations = get_code(info[0], info[1])

n = 20151125
for x in range(round(n_iterations) - 1):
    n = (n * 252533) % 33554393
print(n)