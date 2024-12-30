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
	heapq.heappush(queue, (0, pos_start, dir_start))
	visited = {pos_start}
	
	while queue:
		score, pos_curr, dir_curr = heapq.heappop(queue)
		
		if pos_curr == pos_end:
			return score
		
		for dir_next in directions.values():
			score_directionchange = 0
			if dir_next != dir_curr:
				score_directionchange += 1000
			
			pos_next = tuple(np.add(pos_curr, dir_next))
			if pos_next not in visited and map[pos_next] != '#':
				visited.add(pos_next)
				heapq.heappush(queue, (score + score_directionchange + 1, pos_next, dir_next))
	assert(False)


print(bfs())
