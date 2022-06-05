import re

with open("4.txt") as f:
    for line in f:
        passwords = re.split("\D+", line.strip())

doubles = ["11", "22", "33", "44", "55", "66", "77", "88", "99", "00"]
triples = ["111", "222", "333", "444", "555", "666", "777", "888", "999", "000"]
quadruples = ["1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "0000"]
quintuples = ["11111", "22222", "33333", "44444", "55555", "66666", "77777", "88888", "99999", "00000"]
sextuples = ["111111", "222222", "333333", "444444", "555555", "666666", "777777", "888888", "999999", "000000"]
def validPassword(s):
    double = 0
    for i in range(len(s) - 1):
        if (s[i] + s[i+1]) in doubles:
            double += 1
    if double == 0: 
        return False
    for i in range(len(s) - 1):
        if not int(s[i]) <= int(s[i+1]):
            return False
    return True

validCount = 0
for i in range(int(passwords[0]), int(passwords[1]) + 1):
    if validPassword(str(i)):
        validCount += 1
print(validCount)

def validPasswordv2(s):
    double = 0
    ind = 0
    while ind < 5:
        if not (s[ind] + s[ind + 1]) in doubles:
            ind += 1
        elif (s[ind] + s[ind + 1]) in doubles:
            if ind == 4:
                ind += 2
                double += 1
            elif ind == 3:
                if not ((s[ind] + s[ind + 1] + s[ind + 2]) in triples):
                    ind += 2
                    double += 1
                else:
                    ind += 3
            elif ind == 2:
                if not (((s[ind] + s[ind + 1] + s[ind + 2]) in triples) or ((s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3]) in quadruples)):
                    ind += 2
                    double += 1
                elif (s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3]) in quadruples:
                    ind += 4
                elif (s[ind] + s[ind + 1] + s[ind + 2]) in triples:
                    ind += 3
            elif ind == 1:
                if not (((s[ind] + s[ind + 1] + s[ind + 2]) in triples) or ((s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3]) in quadruples) or ((s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3] + s[ind + 4]) in quintuples)):
                    ind += 2
                    double += 1
                elif (s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3] + s[ind + 4]) in quintuples:
                    ind += 5
                elif (s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3]) in quadruples:
                    ind += 4
                elif (s[ind] + s[ind + 1] + s[ind + 2]) in triples:
                    ind += 3
            elif ind == 0:
                if not (((s[ind] + s[ind + 1] + s[ind + 2]) in triples) or ((s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3]) in quadruples) or ((s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3] + s[ind + 4]) in quintuples) or ((s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3] + s[ind + 4] + s[ind + 5]) in sextuples)):
                    ind += 2
                    double += 1
                elif (s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3] + s[ind + 4] + s[ind + 5]) in sextuples:
                    ind += 6
                elif (s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3] + s[ind + 4]) in quintuples:
                    ind += 5
                elif (s[ind] + s[ind + 1] + s[ind + 2] + s[ind + 3]) in quadruples:
                    ind += 4
                elif (s[ind] + s[ind + 1] + s[ind + 2]) in triples:
                    ind += 3
    if double == 0:
        return False
    for i in range(len(s) - 1):
        if not int(s[i]) <= int(s[i+1]):
            return False
    return True

validCount = 0
for i in range(int(passwords[0]), int(passwords[1]) + 1):
    if validPasswordv2(str(i)):
        validCount += 1
print(validCount)