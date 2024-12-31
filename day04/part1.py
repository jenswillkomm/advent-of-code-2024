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


search_word = 'XMAS'
directions = {(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)}


def verify(pos, dir, word):
	if len(word) <= 0:
		return True
	
	if not (0 <= pos[0] < data.shape[0] and 0 <= pos[1] < data.shape[1]):
		return False
	
	if data[pos] != word[0]:
		return False
	
	return verify((pos[0] + dir[0], pos[1] + dir[1]), dir, word[1:])


data = np.array([list(s) for s in input.splitlines()])


print(sum([verify(tuple(pos), dir, search_word) for pos in np.argwhere(data == 'X') for dir in directions]))
