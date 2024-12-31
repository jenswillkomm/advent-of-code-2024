import numpy as np


input = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
'''

# with open('input', 'r') as f:
# 	input = f.read()


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

map = np.array([list(map(int, list(line))) for line in input.splitlines()])


height_start = 0
height_end = 9
queue = [(tuple(e), tuple(e)) for e in np.argwhere(map == height_start)]
hiking_trails = set()
# There is no need to remember already visited fields since a hiking trail increases by a height of exactly 1 at each step.
while queue:
	pos_trailhead, pos_curr = queue.pop(0)
	if map[pos_curr] == height_end:
		hiking_trails.add((pos_trailhead, pos_curr))
	for direction in directions:
		pos_next = tuple(np.add(pos_curr, direction))
		if 0 <= pos_next[0] < map.shape[0] and 0 <= pos_next[1] < map.shape[1] and map[pos_curr] + 1 == map[pos_next]:
			queue.append((pos_trailhead, pos_next))


print(len(hiking_trails))
