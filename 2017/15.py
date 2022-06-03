with open("15.txt") as f:
	for i, line in enumerate(f):
		inp = line.strip().split()
		if i == 0:
			num1 = int(inp[-1])
		else:
			num2 = int(inp[-1])

num1p2 = num1
num2p2 = num2
fact1 = 16807
fact2 = 48271
div = 2147483647


count = 0
for n in range(40000000):
	num1 = (num1 * fact1) % div
	num2 = (num2 * fact2) % div
	if format(num1, "b")[-16:] == format(num2, "b")[-16:]:
		count += 1
print(count)

count = 0
pairs = 0
while pairs < 5000000:
	while True:
		num1p2 = (num1p2 * fact1) % div
		if num1p2 % 4 == 0:
			break
	while True:
		num2p2 = (num2p2 * fact2) % div
		if num2p2 % 8 == 0:
			break
	if format(num1p2, "b")[-16:] == format(num2p2, "b")[-16:]:
		count += 1
	pairs += 1
print(count)