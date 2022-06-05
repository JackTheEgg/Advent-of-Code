record = []
with open("20.txt") as f:
	for line in f:
		a, b = [int(i) for i in line.strip().split("-")]
		record.append((a, b))

record.sort()
valid, ip, index = [], 0, 0
while ip < 2**32:
    lower, upper = record[index]
    if ip >= lower:
        if ip <= upper:
            ip = upper + 1
            continue
        index += 1
    else:
    	valid.append(ip)
    	ip += 1
print(valid[0])
print(len(valid))