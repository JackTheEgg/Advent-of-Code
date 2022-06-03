import copy

foods = []
with open("21.txt") as f:
    for line in f:
        food = line.strip().split(" (contains ")
        food[0] = food[0].split(" ")
        food[1] = food[1].split(", ")
        foods.append(food)
foodList = copy.deepcopy(foods)

alergFoods = {}
for food in foods:
    for alerg in food[1]:
        if not alerg in alergFoods:
            alergFoods[alerg] = []
for k in alergFoods:
    for food in foods:
        if k in food[1]:
            alergFoods[k].append(food[0])

def common_list_of_lists(lst): # return a list of all common elements on a list of lists
    temp = set(lst[0]).intersection(*lst)
    return list(temp)
     
posAlerg = {}
for alerg, foods in alergFoods.items():
    alergs = common_list_of_lists(foods)
    posAlerg[alerg] = alergs

defAlerg = []
defAlergdict = {}
while len(defAlerg) < len(posAlerg):
    for k, v in posAlerg.items():
        if len(v) == 1:
            defAlerg.append(v[0])
            defAlergdict[k] = v[0]
            needsRemove = v[0]
            break
    for a, b in posAlerg.items():
        if needsRemove in b:
            b.remove(needsRemove)

count = 0
for food in foodList:
    for ingredient in food[0]:
        if not ingredient in defAlerg:
            count += 1
print(count)

sortednames = sorted(defAlergdict.keys())
alerglist = ""
lineCount = 0
for name in sortednames:
    lineCount += 1
    if lineCount != len(sortednames):
        mark = ","
    else:
        mark = ""
    alerglist = alerglist + defAlergdict[name] + mark
print(alerglist)