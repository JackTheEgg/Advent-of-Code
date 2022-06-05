def lookandsay(num):
	result = ""
	repeat = num[0]
	number = num[1:] + " "
	times = 1
	for actual in number:
		if actual != repeat:
			result += str(times) + repeat
			times = 1
			repeat = actual
		else:
			times += 1
	return result

num = open("10.txt").read().strip()

for i in range(50):
	num = lookandsay(num)
	if i == 39:
		print(len(num))
print(len(num))