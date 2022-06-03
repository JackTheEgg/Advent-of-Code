import hashlib

inp = open("5.txt").read().strip()
password1 = ""
for i in range(100000000000):
	if len(password1) == 8:
		break
	test = inp + str(i)
	result = hashlib.md5(test.encode()).hexdigest()
	if result[:5] == "00000":
		password1 += str(result[5])
print(password1)

password2 = ["_" for i in range(8)]
for i in range(100000000000):
	if not "_" in password2:
		break
	test = inp + str(i)
	result = hashlib.md5(test.encode()).hexdigest()
	if result[:5] == "00000":
		if result[5].isnumeric():
			if 0 <= int(result[5]) <= 7:
				if password2[int(result[5])] == "_":
					password2[int(result[5])] = result[6]
print("".join(password2))