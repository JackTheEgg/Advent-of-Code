import hashlib

inp = open("4.txt").read().strip()
leading5, leading6 = None, None
for i in range(100000000000):
	test = inp + str(i)
	result = hashlib.md5(test.encode())
	if result.hexdigest()[:5] == "00000" and not leading5:
		leading5 = i
	if result.hexdigest()[:6] == "000000" and not leading6:
		leading6 = i
		break
print(leading5)
print(leading6)