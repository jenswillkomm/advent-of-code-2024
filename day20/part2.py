import heapq
import itertools
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

min_saving = 50

# with open('input', 'r') as f:
# 	input = f.read()
# 	min_saving = 100


cheating_time = 20

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


reachable_positions = set()
for m, n in itertools.combinations_with_replacement(range(cheating_time + 1), 2):
	if abs(m) + abs(n) <= cheating_time:
		reachable_positions.add((m, n))
		reachable_positions.add((-m, n))
		reachable_positions.add((m, -n))
		reachable_positions.add((-m, -n))
		reachable_positions.add((n, m))
		reachable_positions.add((-n, m))
		reachable_positions.add((n, -m))
		reachable_positions.add((-n, -m))


def get_reachable_positions(pos):
	result = set()
	for p in reachable_positions:
		pos_new = tuple(np.add(pos, p))
		
		if pos_new not in picoseconds:
			continue
		
		result.add(pos_new)
	return result


paths = bfs()
picoseconds = dict([(pos, ps) for ps, pos in paths])
savings = set()
for ps_start, pos_start in paths:
	for pos_end in get_reachable_positions(pos_start):
		saving = picoseconds[pos_end] - (ps_start + (abs(pos_end[0] - pos_start[0]) + abs(pos_end[1] - pos_start[1])))
		if saving >= min_saving:
			savings.add((pos_start, pos_end, saving))


print(len(savings))
