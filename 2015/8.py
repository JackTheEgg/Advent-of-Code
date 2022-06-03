print(sum(len(s.strip()) - len(eval(s)) for s in open("8.txt")))
print(sum(2 + s.count('\\') + s.count('"') for s in open("8.txt")))