from collections import deque, defaultdict

class IntCode:
	def __init__(self, data, inp = None):
		prog = defaultdict(int)
		for i,n in enumerate(data):
			prog[i] = n
		self.prog = prog 
		self.ind = 0
		self.relBase = 0
		self.input = deque() if inp is None else deque(inp)
		self.output = deque()
		self.halted = False

	def getValue(self, mode, ind):
		if mode == "0":
			return self.prog[self.prog.get(ind)]
		elif mode == "1":
			return self.prog[ind]
		elif mode == "2":
			return self.prog[self.prog.get(ind) + self.relBase]
	
	def writeValue(self, mode, ind):
		if mode == "0":
			return self.prog.get(ind)
		elif mode == "2":
			return self.prog.get(ind) + self.relBase

	def run(self, output_and_stop = False):
		while not self.halted:
			val = str(self.prog[self.ind]).zfill(5)
			n1, n2, n3 = val[-3], val[-4], val[-5]
			if val[-1] == "1":
				self.prog[self.writeValue(n3, self.ind + 3)] = self.getValue(n1, self.ind + 1) + self.getValue(n2, self.ind + 2)
				self.ind += 4
			elif val[-1] == "2":
				self.prog[self.writeValue(n3, self.ind + 3)] = self.getValue(n1, self.ind + 1) * self.getValue(n2, self.ind + 2)
				self.ind += 4
			elif val[-1] == "3":
				if not self.input:
					return
				self.prog[self.writeValue(n1, self.ind + 1)] = self.input.popleft()
				self.ind += 2
			elif val[-1] == "4":
				self.output.append(self.getValue(n1, self.ind + 1))
				self.ind += 2
				if output_and_stop:
					return self.output.popleft()
			elif val[-1] == "5":
				if self.getValue(n1, self.ind + 1) != 0:
					self.ind = self.getValue(n2, self.ind + 2)
				else:
					self.ind += 3
			elif val[-1] == "6":
				if self.getValue(n1, self.ind + 1) == 0:
					self.ind = self.getValue(n2, self.ind + 2)
				else:
					self.ind += 3
			elif val[-1] == "7":
				self.prog[self.writeValue(n3, self.ind + 3)] = 1 if self.getValue(n1, self.ind + 1) < self.getValue(n2, self.ind + 2) else 0
				self.ind += 4
			elif val[-1] == "8":
				self.prog[self.writeValue(n3, self.ind + 3)] = 1 if self.getValue(n1, self.ind + 1) == self.getValue(n2, self.ind + 2) else 0
				self.ind += 4
			elif val[-2:] == "99":
				self.halted = True
				return
			elif val[-1] == "9":
				self.relBase += self.getValue(n1, self.ind + 1)
				self.ind += 2