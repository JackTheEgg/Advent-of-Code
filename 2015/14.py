import re
import math

horses = {}
with open("14.txt") as f:
	for line in f:
		horse = line.strip().split(" ")[0]
		info = list(map(int, re.findall("-?[0-9]+", line.strip())))
		horses[horse] = {"speed": info[0], "speedTime": info[1], "restTime": info[2]}

distances = []
for horse, info in horses.items():
	raceTime = 2503
	cycles = raceTime / (info["speedTime"] + info["restTime"]) 
	fullCycles = math.floor(cycles)
	remainder = cycles - fullCycles
	distance = fullCycles * (info["speed"] * info["speedTime"])
	if remainder * (info["speedTime"] + info["restTime"]) >= info["speedTime"]:
		distance += info["speed"] * info["speedTime"]
	else:
		distance += info["speed"] * (remainder * (info["speedTime"] + info["restTime"]))
	distances.append(distance)
distances.sort()
print(distances[-1])

points = {horse:0 for horse in horses.keys()}
distances = {horse:0 for horse in horses.keys()}
cycleTimes = {horse: horses[horse]["speedTime"] + horses[horse]["restTime"] for horse in horses.keys()}
for sec in range(2503):
	for horse, info in horses.items():
		if sec % cycleTimes[horse] < info["speedTime"]:
			distances[horse] += info["speed"]
		else:
			continue
	lead = max(distances.values())
	for horse in horses:
		if distances[horse] == lead:
			points[horse] += 1
print(max(points.values()))