from collections import deque

cards = deque([i for i in range(10007)])

def dealIncr(cards, incr):
	i = 0
	newCards = list(cards.copy())
	while cards:
		card = cards.popleft()
		newCards[i] = card
		i = (i + incr) % len(newCards)
	return newCards

for line in open("22.txt").readlines():
	if line.strip() == "deal into new stack":
		cards.reverse()
	elif line.startswith("cut"):
		n = int(line.strip().split()[-1])
		if n < 0:
			cards.rotate(abs(n))
		else:
			stack = [cards.popleft() for i in range(n)]
			cards.extend(stack)
	elif line.startswith("deal"):
		incr = int(line.strip().split()[-1])
		cards = deque(dealIncr(cards, incr))
print(list(cards).index(2019))

m = 119315717514047
n = 101741582076661
pos = 2020
shuffles = { 'deal with increment ': lambda x,m,a,b: (a*x %m, b*x %m),
         'deal into new stack': lambda _,m,a,b: (-a %m, (m-1-b)%m),
         'cut ': lambda x,m,a,b: (a, (b-x)%m) }
a,b = 1,0
with open("22.txt") as f:
  for s in f.read().strip().split('\n'):
    for name,fn in shuffles.items():
      if s.startswith(name):
        arg = int(s[len(name):]) if name[-1] == ' ' else 0
        a,b = fn(arg, m, a, b)
        break
r = (b * pow(1-a, m-2, m)) % m
print(((pos - r) * pow(a, n*(m-2), m) + r) % m)