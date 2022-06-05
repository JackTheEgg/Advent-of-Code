passports = []
passport = {}
with open("4.txt") as inp:
    for line in inp:
        if line != "\n":
            line = line.rstrip().split(" ")
            line = [field.split(":") for field in line]
            for field in line:
                passport[field[0]] = field[1]
        else:
            passports.append(passport)
            passport = {}
    passports.append(passport)

validPassports = 0
for passport in passports:
    fieldCount = 0
    for key in passport.keys():
        fieldCount += 1
    if fieldCount == 8 or (fieldCount == 7 and (not "cid" in passport)):
        validPassports += 1
print(validPassports)

colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth",]

def checkHeight(s):
    if s[-2:] == "cm":
        if 150 <= int(s[:-2]) <= 193:
            return True
        else:
            return False
    elif s[-2:] == "in":
        if 59 <= int(s[:-2]) <= 76:
            return True
        else:
            return False
    else:
        return False

validPassports = 0
for passport in passports:
    fieldCount = 0
    for key in passport.keys():
        fieldCount += 1
    if fieldCount == 8 or (fieldCount == 7 and (not "cid" in passport)):
        if (1920 <= int(passport["byr"]) <= 2002) \
        and (2010 <= int(passport["iyr"]) <= 2020) \
        and (2020 <= int(passport["eyr"]) <= 2030) \
        and (checkHeight(passport["hgt"]))\
        and ((passport["hcl"][0] == "#") and (len(passport["hcl"]) == 7)) \
        and (passport["ecl"] in colors) \
        and (passport["pid"].isnumeric() and len(passport["pid"]) == 9):
            validPassports += 1
print(validPassports)