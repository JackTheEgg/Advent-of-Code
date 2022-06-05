from datetime import datetime
import re 
from collections import Counter
import sys

times = []
with open("4.txt") as f:
	for line in f:
		times.append(re.search("\[(.+)\]", line.strip())[1])

fmt = "%Y-%m-%d %H:%M"
times = [datetime.strptime(ts, fmt) for ts in times]
times.sort()
times = [datetime.strftime(ts, fmt) for ts in times]

timeline = []
for time in times:
	with open("4.txt") as f:
		for line in f:
			if re.search("\[(.+)\]", line.strip())[1] == time:
				timeline.append(line.strip())
				break

guards = {}
for event in timeline:
	if "Guard" in event:
		nums = list(map(int, re.findall("-?[0-9]+", event)))
		if not nums[-1] in guards:
			guards[nums[-1]] = {"sleepTime":0, "sleepMins":[]}
			guard = nums[-1]
		else:
			guard = nums[-1]
	elif "falls asleep" in event:
		t = re.search("\[(.+)\]", event)[1]
		start = datetime.strptime(t, fmt)
	elif "wakes up" in event:
		t = re.search("\[(.+)\]", event)[1]
		end = datetime.strptime(t, fmt)
		df = end - start
		guards[guard]["sleepTime"] += int(round(df.total_seconds() / 60))
		for i in range(start.minute, end.minute):
			guards[guard]["sleepMins"].append(i)

maxSleep = max(v["sleepTime"] for v in guards.values())
for guard, info in guards.items():
	if info["sleepTime"] == maxSleep:
		mostCommonMinute = Counter(info["sleepMins"]).most_common(1)
		print(mostCommonMinute[0][0] * guard)
		break

sleepMins = {}
for guard, info in guards.items():
	minutes = Counter(info["sleepMins"]).most_common()
	if len(minutes) > 0:
		a = {}
		for pair in minutes:
			a[pair[0]] = pair[1]
		sleepMins[guard] = a

mins = [i for i in range(60)]
maxCommonMins = {}
for m in mins:
	count = 0
	for g, i in sleepMins.items():
		if m in i:
			count += 1
	if count == len(sleepMins):
		maxCommonMins[m] = max(sleepMins[a][m] for a in sleepMins.keys())

for k, v in maxCommonMins.items():
	if v == max(maxCommonMins.values()):
		targetMin = k
		targetTimes = v
		break

for g, i in sleepMins.items():
	for k, v in i.items():
		if k == targetMin and v == targetTimes:
			print(g * targetMin)
			sys.exit()