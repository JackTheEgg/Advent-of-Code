passwords = []
with open("2.txt") as file:
    for line in file:
        password = line.split(" ")
        passwords.append(password)

count = 0
for password in passwords:
    letterCount = 0
    for letter in password[3]:
        if letter == password[2]:
            letterCount += 1
    if int(password[0]) <= letterCount <= int(password[1]):
        count += 1
print(count)

count = 0
for password in passwords:
    if password[3][int(password[0])-1] == password[2] or password[3][int(password[1])-1] == password[2]:
        if not (password[3][int(password[0])-1] == password[2] and password[3][int(password[1])-1] == password[2]):
            count += 1
print(count)