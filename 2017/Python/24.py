from copy import deepcopy

pins = []
with open("24.txt") as f:
	for line in f:
		pins.append(list(map(int, line.strip().split("/"))))

def connect(bridges):
	newBridges = []
	for b in bridges:
		for pin in pins:
			rp = pin[::-1]
			if b[-1][1] == pin[0] and not (pin in b or rp in b):
				newb = deepcopy(b)
				newb.append(pin)
				newBridges.append(newb)
			elif b[-1][1] == rp[0] and not (pin in b or rp in b):
				newb = deepcopy(b)
				newb.append(rp)
				newBridges.append(newb) 
	return newBridges

def strength(bridge):
	return sum(sum(pair) for pair in bridge)

bridges = [[[0,0]]]
strengths = []
while len(bridges) > 0:
	longest = len(bridges)
	bridges = connect(bridges)
	for bridge in bridges:
		strengths.append(strength(bridge))
print(max(strengths))
print(max(strengths[-longest:]))