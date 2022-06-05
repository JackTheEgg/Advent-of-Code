import re
from json import loads

inp1 = open("12.txt").read().strip()
inp2 = loads(inp1)

nums = list(map(int, re.findall("-?[0-9]+", inp1)))
print(sum(nums))

def nums(js):
	if type(js) == int:
		return js
	if type(js) == list:
		return sum([nums(i) for i in js])
	if type(js) != dict:
		return 0
	if "red" in js.values():
		return 0
	return nums(list(js.values()))
print(nums(inp2))