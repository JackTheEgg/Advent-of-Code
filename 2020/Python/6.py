groups = []
group = []
with open("6.txt") as file:
    for line in file:
        if line != "\n":
            group.append(line.strip())
        else:
            groups.append(group)
            group = []
    groups.append(group)

counts = []
for group in groups:
    answered = []
    for questions in group:
        for letters in questions:
            if not letters in answered:
                answered.append(letters)
    counts.append(len(answered))

count = 0
for values in counts:
    count += values
print(count)

letters = "abcdefghijklmnopqrstuvwxyz"
questionCount = 0
for group in groups:
    for letter in letters:
        letterCount = 0
        for questions in group:
            if letter in questions:
                letterCount += 1
        if letterCount == len(group):
            questionCount += 1
print(questionCount)