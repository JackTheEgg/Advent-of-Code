ingrs = {}
with open("15.txt") as f:
	for line in f:
		inp = line.strip().split(" ")
		info = {inp[1:][i]: int(inp[1:][i+1][:-1]) for i in range(0, len(inp[1:]) - 2, 2)}
		info[inp[1:][8]] = int(inp[1:][9])
		ingrs[inp[0][:-1]] = info

def multichoose(n, k): #ways to pick n elements that add up to k
	if not k: return [[0]*n]
	if not n: return []
	if n == 1: return [[k]]
	return [[0] + val for val in multichoose(n-1, k)] + \
			[[val[0] + 1] + val[1:] for val in multichoose(n,k-1)]

def cookieScore(amounts, ingrs):
	capacity = sum(amounts[i]*ingrs[list(ingrs.keys())[i]]["capacity"] for i in range(len(amounts))) > 0 and sum(amounts[i]*ingrs[list(ingrs.keys())[i]]["capacity"] for i in range(len(amounts))) or 0
	durability = sum(amounts[i]*ingrs[list(ingrs.keys())[i]]["durability"] for i in range(len(amounts))) > 0 and sum(amounts[i]*ingrs[list(ingrs.keys())[i]]["durability"] for i in range(len(amounts))) or 0
	flavor = sum(amounts[i]*ingrs[list(ingrs.keys())[i]]["flavor"] for i in range(len(amounts))) > 0 and sum(amounts[i]*ingrs[list(ingrs.keys())[i]]["flavor"] for i in range(len(amounts))) or 0
	texture = sum(amounts[i]*ingrs[list(ingrs.keys())[i]]["texture"] for i in range(len(amounts))) > 0 and sum(amounts[i]*ingrs[list(ingrs.keys())[i]]["texture"] for i in range(len(amounts))) or 0
	calories = sum(amounts[i]*ingrs[list(ingrs.keys())[i]]["calories"] for i in range(len(amounts))) > 0 and sum(amounts[i]*ingrs[list(ingrs.keys())[i]]["calories"] for i in range(len(amounts))) or 0
	return capacity*durability*flavor*texture, calories

ways = multichoose(4,100)
scores = []
calories = []

for amounts in ways:
	score, calory = cookieScore(amounts, ingrs)
	scores.append(score)
	calories.append(calory)
print(max(scores))

indexes = []
for index, amount in enumerate(calories):
	if amount == 500:
		indexes.append(index)
print(int(max(scores[i] for i in indexes)))