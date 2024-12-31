import re
from collections import Counter
import numpy as np


input = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
'''

space_limits = (11, 7)

# with open('input', 'r') as f:
# 	input = f.read()
# 	space_limits = (101, 103)


class Robot:
	def __init__(self, position, velocity):
		self.pos = position
		self.velocity = velocity
	
	def simulate(self):
		self.pos = tuple((np.add(self.pos, self.velocity) + space_limits) % space_limits)


def parse(s):
	m = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', s)
	assert(m)
	return Robot((int(m[1]), int(m[2])), (int(m[3]), int(m[4])))


robots = [parse(line) for line in input.splitlines()]

i = 0
while max(Counter([robot.pos for robot in robots]).values()) > 1:
	for r in robots:
		r.simulate()
	i += 1


print(i)
