import re
import numpy as np


input = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
'''

# with open('input', 'r') as f:
# 	input = f.read()


class Claw_Machine:
	def __init__(self, description):
		self.movement_button = {}
		self.pos_prize = (0, 0)
		
		for line in description.splitlines():
			key, value = line.split(': ')
			if key == 'Prize':
				m = re.match(r'X=(\d+), Y=(\d+)', value)
				self.pos_prize = (int(m[1]) + 10000000000000, int(m[2]) + 10000000000000)
			else:
				m = re.match(r'Button ([AB]): X\+(\d+), Y\+(\d+)', line)
				self.movement_button[m[1]] = (int(m[2]), int(m[3]))
	
	def solve(self):
		a = np.transpose([self.movement_button['A'], self.movement_button['B']])
		b = self.pos_prize
		x = np.round(np.linalg.solve(a, b))
		
		if not np.all(a @ x == b):
			return 0
		
		return int(np.inner(x, [3, 1]))


claw_machines = [Claw_Machine(s) for s in input.split('\n\n')]


print(sum([cm.solve() for cm in claw_machines]))
