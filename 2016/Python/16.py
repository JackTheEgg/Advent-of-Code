change = {"1":"0", "0":"1"}

def dCurve(a):
	b = str(a)
	b = b[::-1]
	invb = ""
	for char in b:
		invb += change[char]
	return a + "0" + invb	

def checkSum(s):
	new = ""
	for i in range(0, len(s), 2):
		if s[i] + s[i+1] == "00" or s[i] + s[i+1] == "11":
			new += "1"
		else:
			new += "0"
	return new

length = 272
start = open("16.txt").read().strip()
while len(start) < length:
	start = dCurve(start)

check = start[:length]
while len(check) % 2 == 0:
	check = checkSum(check)
print(check)

length = 35651584
start = open("16.txt").read().strip()
while len(start) < length:
	start = dCurve(start)

check = start[:length]
while len(check) % 2 == 0:
	check = checkSum(check)
print(check)