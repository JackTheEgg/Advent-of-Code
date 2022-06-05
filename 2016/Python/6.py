lines = []
with open("6.txt") as f:
	for line in f:
		lines.append(line.strip())

def mostCommon(lst):
	return max(set(lst), key = lst.count)

def leastCommon(lst):
	return min(set(lst), key = lst.count)

word1 = ""
word2 = ""
for i in range(len(lines[0])):
	letters = [line[i] for line in lines]
	word1 += mostCommon(letters)
	word2 += leastCommon(letters)
print(word1)
print(word2)