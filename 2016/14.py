import hashlib
import string

inp = open("14.txt").read().strip()
chars = string.ascii_lowercase + string.digits
trips = [3*char for char in chars]
quints = [5*char for char in chars]

def genHashes(inp, keyCount, stretch = False):
	for i in range(100000000000):
		test = inp + str(i)
		result = hashlib.md5(test.encode()).hexdigest()
		if stretch:
			for n in range(2016):
				result = hashlib.md5(result.encode()).hexdigest()
		triple = None
		for k in range(len(result) - 2):
			if result[k:k+3] in trips:
				triple = result[k:k+3]
				break
		if triple:
			for j in range(i + 1, i + 1000 + 1):
				test2 = inp + str(j) 
				result2 = hashlib.md5(test2.encode()).hexdigest()
				if stretch:
					for n in range(2016):
						result2 = hashlib.md5(result2.encode()).hexdigest()
				if quints[trips.index(triple)] in result2:
					keyCount += 1
					break
		if keyCount == 64:
			return i

print(genHashes(inp, 0))
print(genHashes(inp, 0, True))