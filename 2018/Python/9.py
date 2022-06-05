from collections import deque, defaultdict
import re

nums = list(map(int, re.findall("-?[0-9]+", open("9.txt").read().strip())))
players, limit = nums[0], nums[1]

def play(players, limit):
	scores = defaultdict(int)
	marbles = deque([0])
	for marble in range(1, limit):
		if marble % 23 == 0:
			marbles.rotate(7)
			scores[marble % players] += marble + marbles.pop()
			marbles.rotate(-1)
		else:
			marbles.rotate(-1)
			marbles.append(marble)
	print(max(scores.values()))

play(players, limit)
play(players, limit * 100)