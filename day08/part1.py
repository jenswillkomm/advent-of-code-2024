import numpy as np
import itertools


input = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''

# with open('input', 'r') as f:
# 	input = f.read()


def get_position_antinodes(frequency):
	result = set()
	
	for pos_antenna1, pos_antenna2 in itertools.combinations(np.argwhere(map == frequency), 2):
		delta = np.subtract(pos_antenna2, pos_antenna1)
		result.add(tuple(np.subtract(pos_antenna1, delta)))
		result.add(tuple(np.add(pos_antenna2, delta)))
	
	return result


map = np.array([list(row) for row in input.splitlines()])
frequencies = set(map.flatten()) - set('.')

pos_antinodes = {p for f in frequencies for p in get_position_antinodes(f) if 0 <= p[0] < map.shape[0] and 0 <= p[1] < map.shape[1]}


print(len(pos_antinodes))
