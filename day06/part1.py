import numpy as np


input = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''

# with open('input', 'r') as f:
# 	input = f.read()


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # (y, x)


map = np.array([list(row) for row in input.splitlines()])
pos_start = np.argwhere(map == '^')
assert(len(pos_start) == 1)
pos_curr = tuple(pos_start[0])
dir_curr = directions[0]
visited = {pos_curr}

while True:
	pos_next = tuple(np.add(pos_curr, dir_curr))
	
	if not (pos_next[0] in range(map.shape[0]) and pos_next[1] in range(map.shape[1])):
		break
	
	if map[pos_next] == '#':
		dir_curr = directions[(directions.index(dir_curr) + 1) % len(directions)]  # turn right
		continue
	
	pos_curr = pos_next
	visited.add(pos_curr)


print(len(visited))
