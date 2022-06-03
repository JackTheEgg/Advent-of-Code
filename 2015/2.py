def getPaper(lst):
	return 2*lst[0]*lst[1] + 2*lst[1]*lst[2] + 2*lst[0]*lst[2] + min([lst[0]*lst[1], lst[1]*lst[2], lst[0]*lst[2]])

def getRibbon(lst):
	return min([2*lst[0] + 2*lst[1], 2*lst[1] + 2*lst[2], 2*lst[2] + 2*lst[0]]) + (lst[0]*lst[1]*lst[2])

totalP = 0
totalR = 0
with open("2.txt") as f:
	for line in f:
		dim = list(map(int, line.strip().split("x")))
		totalP += getPaper(dim)
		totalR += getRibbon(dim)
print(totalP)
print(totalR)