import re

def gen_regex(r="0", depth=15):
    if depth == 0:
        return ""
    if rules[r][0][0].startswith('"'):
        return rules[r][0][0].strip('"')
    return "(" + "|".join(["".join([gen_regex(sub, depth - 1) for sub in subrule]) for subrule in rules[r]]) + ")"


with open("19.txt") as f:
    rules_raw, msgs = f.read().split("\n\n")

rules = {}
for rule in rules_raw.split("\n"):
    num, r = rule.split(": ")
    rules[num] = [s.split() for s in r.split(" | ")]

r1 = re.compile(gen_regex())
res = [r1.fullmatch(msg) for msg in msgs.split("\n")]
print(len([x for x in res if x]))

rules["8"] = [["42"], ["42", "8"]]
rules["11"] = [["42", "31"], ["42", "11", "31"]]

r2 = re.compile(gen_regex())
res = [r2.fullmatch(msg) for msg in msgs.split("\n")]
print(len([x for x in res if x]))