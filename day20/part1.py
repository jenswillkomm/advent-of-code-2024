import heapq
import numpy as np


input = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
'''

min_saving = 1

# with open('input', 'r') as f:
# 	input = f.read()
# 	min_saving = 100


map = np.array([list(row) for row in input.splitlines()])
pos_start = tuple(np.argwhere(map == 'S')[0])
pos_end = tuple(np.argwhere(map == 'E')[0])

directions = {
	'up': (-1, 0),
	'down': (1, 0),
	'left': (0, -1),
	'right': (0, 1)
}


def bfs():
	queue = [[(0, pos_start)]]
	heapq.heapify(queue)
	visited = set()
	while queue:
		path = heapq.heappop(queue)
		picosecond, pos = path[-1]
		
		if pos == pos_end:
			return path
		
		for dir in directions.values():
			pos_next = tuple(np.add(pos, dir))
			if map[pos_next] != '#' and pos_next not in visited:
				visited.add(pos_next)
				heapq.heappush(queue, path + [(picosecond + 1, pos_next)])
	return []


paths = bfs()
picoseconds = dict([(pos, ps) for ps, pos in paths])
savings = set()
for ps_start, pos_start in paths:
	for dir in directions.values():
		pos_end = tuple(np.add(pos_start, np.multiply(dir, 2)))
		if pos_end in picoseconds:
			saving = picoseconds[pos_end] - (ps_start + 2)
			if saving >= min_saving:
				savings.add((pos_start, pos_end, saving))


print(len(savings))
