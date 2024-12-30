import numpy as np


input = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''

# with open('input', 'r') as f:
# 	input = f.read()


x_positions = {(-1, -1), (-1, 1), (1, -1), (1, 1)}


def verify(pos):
	if data[pos] != 'A':
		return False
	
	x_neighbors = [data[pos[0] + p[0], pos[1] + p[1]] for p in x_positions if 0 <= pos[0] + p[0] < data.shape[0] and 0 <= pos[1] + p[1] < data.shape[1]]
	if x_neighbors.count('M') == 2 and x_neighbors.count('S') == 2 and x_neighbors[1] != x_neighbors[2]:  # no 'MAM' or 'SAS'
		return True
	return False


data = np.array([list(s) for s in input.splitlines()])


print(sum([verify(tuple(pos)) for pos in np.argwhere(data == 'A')]))
