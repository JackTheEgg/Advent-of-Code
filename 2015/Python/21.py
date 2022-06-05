from itertools import combinations
import copy

bossStats = {}
with open("21.txt") as f:
	for line in f:
		stat, amount = line.strip().split(": ")
		bossStats[stat] = int(amount)

playerStats = {"Hit Points": 100, "Damage": 0, "Armor": 0}

shop = { # 0 = cost, 1 = damage, 2 = armor
	"Weapons": {"Dagger": [8, 4, 0], "Shortsword": [10, 5, 0], "Warhammer": [25, 6, 0], "Longsword": [40, 7, 0], "Greataxe": [74, 8, 0]},
	"Armor": {"Leather": [13, 0, 1], "Chainmail": [31, 0, 2], "Splintmail": [53, 0, 3], "Bandedmail": [75, 0, 4], "Platemail": [102, 0, 5]},
	"Rings": {"Damage +1": [25, 1, 0], "Damage +2": [50, 2, 0], "Damage +3": [100, 3, 0], "Defense +1": [20, 0, 1], "Defense +2": [40, 0, 2], "Defense +3": [80, 0, 3]},
}

def getAllWays(lst, n1, n2):
	ways = []
	for i in range(n1, n2+1):
		ways += list(combinations(lst, i))
	return ways

weaponCombs = getAllWays(list(shop["Weapons"].keys()), 1, 1)
armorCombs = getAllWays(list(shop["Armor"].keys()), 0, 1)
ringCombs = getAllWays(list(shop["Rings"].keys()), 0, 2)

globalCombs = []
for i in range(len(weaponCombs)):
	for j in range(len(armorCombs)):
		for k in range(len(ringCombs)):
			comb = []
			for item in weaponCombs[i]:
				comb.append(item)
			for item in armorCombs[j]:
				comb.append(item)
			for item in ringCombs[k]:
				comb.append(item)
			globalCombs.append(comb)

def turn(player, boss):
	boss["Hit Points"] -= player["Damage"] - boss["Armor"] > 1 and player["Damage"] - boss["Armor"] or 1
	if boss["Hit Points"] <= 0:
		return "Win", 0
	else:
		player["Hit Points"] -= boss["Damage"] - player["Armor"] > 1 and boss["Damage"] - player["Armor"] or 1
		if player["Hit Points"] <= 0:
			return "Lose", 0
		else:
			return player, boss

outcomes = []
for comb in globalCombs:
	cost = 0
	player = copy.deepcopy(playerStats)
	boss = copy.deepcopy(bossStats)
	for item in comb:
		if item in shop["Weapons"]:
			cost += shop["Weapons"][item][0]
			player["Damage"] += shop["Weapons"][item][1]
			player["Armor"] += shop["Weapons"][item][2]
		elif item in shop["Armor"]:
			cost += shop["Armor"][item][0]
			player["Damage"] += shop["Armor"][item][1]
			player["Armor"] += shop["Armor"][item][2]		
		elif item in shop["Rings"]:
			cost += shop["Rings"][item][0]
			player["Damage"] += shop["Rings"][item][1]
			player["Armor"] += shop["Rings"][item][2]
	while player != "Win" and player != "Lose":
		player, boss = turn(player, boss)
	outcomes.append([cost, player])

wins = []
for outcome in outcomes:
	if outcome[1] == "Win":
		wins.append(outcome)
print(min(win[0] for win in wins))

loses = []
for outcome in outcomes:
	if outcome[1] == "Lose":
		loses.append(outcome)
print(max(lose[0] for lose in loses))