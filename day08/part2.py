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
		result.add(tuple(pos_antenna1))
		result.add(tuple(pos_antenna2))
		
		delta = np.subtract(pos_antenna2, pos_antenna1)
		
		pos_antinode = tuple(np.subtract(pos_antenna1, delta))
		while 0 <= pos_antinode[0] < map.shape[0] and 0 <= pos_antinode[1] < map.shape[1]:
			result.add(pos_antinode)
			pos_antinode = tuple(np.subtract(pos_antinode, delta))
		
		pos_antinode = tuple(np.add(pos_antenna2, delta))
		while 0 <= pos_antinode[0] < map.shape[0] and 0 <= pos_antinode[1] < map.shape[1]:
			result.add(pos_antinode)
			pos_antinode = tuple(np.add(pos_antinode, delta))
	
	return result


map = np.array([list(row) for row in input.splitlines()])
frequencies = set(map.flatten()) - set('.')

pos_antinodes = {p for f in frequencies for p in get_position_antinodes(f)}


print(len(pos_antinodes))
