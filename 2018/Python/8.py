from collections import deque

node = deque(list(map(int, open("8.txt").read().strip().split())))
entries, layers, layer = [], {}, 1

def checkLayer(layer):
	s = []
	for i in range(layers[layer - 1][-1][1]):
		v = node.popleft()
		entries.append(v)
		if v <= len(layers[layer - 1][-1][2]) - 1:
			s.append(layers[layer - 1][-1][2][v])
		elif v == 0:
			continue
	layers[layer - 1].pop()
	if sum(len(i) for i in layers.values()) == 0:
		return sum(s)
	if layer - 2 in layers:
		layer -= 1
		layers[layer - 1][-1][2].append(sum(s))
		layers[layer - 1][-1][0] -= 1
		if layers[layer - 1][-1][0] == 0:
			return checkLayer(layer)
		else:
			return layer
	else:
		return layer - 1

while len(node) > 0:
	cNode = node.popleft()
	mEntr = node.popleft()
	if cNode == 0:
		s = []
		for i in range(mEntr):
			val = node.popleft()
			entries.append(val)
			s.append(val)
		layers[layer - 1][-1][0] -= 1
		layers[layer - 1][-1][2].append(sum(s))
		if layers[layer - 1][-1][0] == 0:
			layer = checkLayer(layer)
	elif not layer in layers:
		layers[layer] = deque([[cNode, mEntr, [0]]])
		layer += 1
	else:
		layers[layer].append([cNode, mEntr, [0]])
		layer += 1
print(sum(entries))
print(layer)