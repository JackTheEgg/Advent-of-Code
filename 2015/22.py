import random
import copy

bossStats = {}
with open("22.txt") as f:
	for line in f:
		l = line.strip().split(": ")
		bossStats[l[0]] = int(l[1])
playerStats = {"Hit Points": 50, "Mana": 500, "Armor": 0}
spells = {"Magic Missile": 53, "Drain": 73, "Shield": 113, "Poison": 173, "Recharge": 229}
remaining = {"Shield": 0, "Poison": 0, "Recharge": 0}
actives = []
minimum = min(spells.values())

def pickSpell():
	return random.choice(list(spells.keys()))

def buffCheck(player, boss, rem, active):
	for spell in active:
		if spell == "Poison":
			boss["Hit Points"] -= 3
			if boss["Hit Points"] <= 0:
				return "Win", 0, 0, 0 
			rem[spell] -= 1
			if rem[spell] == 0:
				active.remove(spell)
		elif spell == "Shield":
			rem[spell] -= 1
			if rem[spell] == 0:
				player["Armor"] = 0
				active.remove(spell)
		elif spell == "Recharge":
			player["Mana"] += 101
			rem[spell] -= 1
			if rem[spell] == 0:
				active.remove(spell)
	return player, boss, rem, active 

def turn(player, boss, rem, active, spentMana, hardMode = False):
	if hardMode:
		player["Hit Points"] -= 1
		if player["Hit Points"] <= 0:
			return "Lose", boss, rem, active, spentMana
	player, boss, rem, active = buffCheck(player, boss, rem, active)
	if player == "Win":
		return "Win", boss, rem, active, spentMana
	if player["Mana"] < minimum:
		return "Lose", boss, rem, active, spentMana
	cast = pickSpell()
	while (cast in active) or (player["Mana"] < spells[cast]):
		cast = pickSpell()
	if cast == "Magic Missile":
		boss["Hit Points"] -= 4
		player["Mana"] -= spells[cast]
		spentMana += spells[cast]
		if boss["Hit Points"] <= 0:
			return "Win", boss, rem, active, spentMana
	elif cast == "Drain":
		boss["Hit Points"] -= 2
		player["Mana"] -= spells[cast]
		spentMana += spells[cast]
		player["Hit Points"] += 2
		if boss["Hit Points"] <= 0:
			return "Win", boss, rem, active, spentMana
	elif cast == "Shield":
		player["Armor"] = 7
		player["Mana"] -= spells[cast]
		spentMana += spells[cast]
		active.append(cast)
		rem[cast] = 6
	elif cast == "Poison":
		player["Mana"] -= spells[cast]
		spentMana += spells[cast]
		active.append(cast)
		rem[cast] = 6
	elif cast == "Recharge":
		player["Mana"] -= spells[cast]
		spentMana += spells[cast]
		active.append(cast)
		rem[cast] = 5
	player, boss, rem, active = buffCheck(player, boss, rem, active)
	if player == "Win":
		return "Win", boss, rem, active, spentMana
	else:
		player["Hit Points"] -= boss["Damage"] - player["Armor"] > 1 and boss["Damage"] - player["Armor"] or 1
		if player["Hit Points"] <= 0:
			return "Lose", boss, rem, active, spentMana
		else:
			return player, boss, rem, active, spentMana

outcomesp1 = set()
outcomesp2 = set()
for n in range(100000):
	spentMana = 0
	player, boss, rem, active = copy.deepcopy(playerStats), copy.deepcopy(bossStats), copy.deepcopy(remaining), copy.deepcopy(actives)
	while isinstance(player, dict):
		player, boss, rem, active, spentMana = turn(player, boss, rem, active, spentMana)
	outcomesp1.add((spentMana, player))
	spentMana = 0
	player, boss, rem, active = copy.deepcopy(playerStats), copy.deepcopy(bossStats), copy.deepcopy(remaining), copy.deepcopy(actives)
	while isinstance(player, dict):
		player, boss, rem, active, spentMana = turn(player, boss, rem, active, spentMana, True)
	outcomesp2.add((spentMana, player))

winsp1 = []
winsp2 = []
for outcome in outcomesp1:
	if outcome[1] == "Win":
		winsp1.append(outcome)
for outcome in outcomesp2:
	if outcome[1] == "Win":
		winsp2.append(outcome)
print(min(win[0] for win in winsp1)) # 900
print(min(win[0] for win in winsp2)) # 1216