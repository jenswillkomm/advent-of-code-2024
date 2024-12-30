import heapq
import numpy as np


input = '''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
'''

# with open('input', 'r') as f:
# 	input = f.read()


map = np.array([list(line) for line in input.splitlines()])

directions = {
	'north': (-1, 0),
	'south': (1, 0),
	'west': (0, -1),
	'east': (0, 1)
}

pos_start = tuple(np.argwhere(map == 'S')[0])
dir_start = directions['east']
pos_end = tuple(np.argwhere(map == 'E')[0])


def bfs():
	queue = []
	heapq.heappush(queue, (0, [pos_start], dir_start))
	visited = {(pos_start, dir_start): 0}
	score_best_path = np.inf
	best_path_tiles = set()
	
	while queue and queue[0][0] <= score_best_path:
		score, path, dir_curr = heapq.heappop(queue)
		pos_curr = path[-1]
		
		if pos_curr == pos_end:
			if score_best_path == np.inf:
				score_best_path = score
			best_path_tiles |= set(path)
		
		for dir_next in directions.values():
			score_directionchange = 0
			if dir_next != dir_curr:
				score_directionchange += 1000
			
			pos_next = tuple(np.add(pos_curr, dir_next))
			score_next = score + score_directionchange + 1
			if ((pos_next, dir_next) not in visited or visited[(pos_next, dir_next)] >= score_next) and map[pos_next] != '#':
				visited[(pos_next, dir_next)] = score_next
				heapq.heappush(queue, (score_next, path + [pos_next], dir_next))
	
	return len(best_path_tiles)


print(bfs())
