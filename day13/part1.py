import re
from math import inf
from functools import cache


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
				self.pos_prize = (int(m[1]), int(m[2]))
			else:
				m = re.match(r'Button ([AB]): X\+(\d+), Y\+(\d+)', line)
				self.movement_button[m[1]] = (int(m[2]), int(m[3]))


@cache
def dp(claw_machine, times_buttons_pressed, pos_curr):
	if max(times_buttons_pressed) > 100:
		return inf
	
	if pos_curr[0] > claw_machine.pos_prize[0] or pos_curr[1] > claw_machine.pos_prize[1]:
		return inf
	
	if pos_curr == claw_machine.pos_prize:
		return times_buttons_pressed[0] * 3 + times_buttons_pressed[1] * 1
	
	press_a = dp(claw_machine, (times_buttons_pressed[0] + 1, times_buttons_pressed[1]), (pos_curr[0] + claw_machine.movement_button['A'][0], pos_curr[1] + claw_machine.movement_button['A'][1]))
	press_b = dp(claw_machine, (times_buttons_pressed[0], times_buttons_pressed[1] + 1), (pos_curr[0] + claw_machine.movement_button['B'][0], pos_curr[1] + claw_machine.movement_button['B'][1]))
	
	return min(press_a, press_b)


claw_machines = [Claw_Machine(s) for s in input.split('\n\n')]


print(sum([dp(cm, (0, 0), (0, 0)) for cm in claw_machines if dp(cm, (0, 0,), (0, 0)) < inf]))
