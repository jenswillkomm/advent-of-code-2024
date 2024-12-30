import re
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


def parse(s):
	m = re.match(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', s)
	assert(m)
	return Robot((int(m[1]), int(m[2])), (int(m[3]), int(m[4])))


def simulate(robot):
	robot.pos = (np.add(robot.pos, np.multiply(robot.velocity, 100)) + np.multiply(space_limits, 100)) % space_limits
	return robot


def quadrant(robot):
	if robot.pos[0] < np.floor(space_limits[0] / 2) and robot.pos[1] < np.floor(space_limits[1] / 2):
		return 2
	if robot.pos[0] > np.floor(space_limits[0] / 2) and robot.pos[1] < np.floor(space_limits[1] / 2):
		return 1
	if robot.pos[0] > np.floor(space_limits[0] / 2) and robot.pos[1] > np.floor(space_limits[1] / 2):
		return 4
	if robot.pos[0] < np.floor(space_limits[0] / 2) and robot.pos[1] > np.floor(space_limits[1] / 2):
		return 3
	# don't count as being in any quadrant
	return 0


robots = [parse(line) for line in input.splitlines()]
robots = [simulate(robot) for robot in robots]
quadrants = [quadrant(robot) for robot in robots]


print(np.prod([quadrants.count(q) for q in range(1, 5)]))
