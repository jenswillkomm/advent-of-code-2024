import re
import heapq
import numpy as np


input = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
'''

x_max = y_max = 6
simulate_bytes = 12

# with open('input', 'r') as f:
# 	input = f.read()
# 	x_max = y_max = 70
# 	simulate_bytes = 1024


falling_bytes = []
for line in input.splitlines():
	m = re.match(r'(\d+),(\d+)', line)
	falling_bytes.append((int(m[1]), int(m[2])))

directions = {
	'U': (0, 1),
	'D': (0, -1),
	'L': (-1, 0),
	'R': (1, 0)
}

pos_start = (0, 0)
pos_end = (x_max, y_max)

corrupted_coordinates = set(falling_bytes[:simulate_bytes])


def bfs():
	queue = [(0, pos_start)]
	heapq.heapify(queue)
	visited = {pos_start}
	
	while len(queue) > 0:
		step, pos = heapq.heappop(queue)
		
		if pos == pos_end:
			return step
		
		for dir in directions.values():
			pos_next = tuple(np.add(pos, dir))
			
			if pos_next[0] not in range(x_max + 1) or pos_next[1] not in range(y_max + 1):
				continue
			
			if pos_next not in visited and pos_next not in corrupted_coordinates:
				visited.add(pos_next)
				heapq.heappush(queue, (step + 1, pos_next))
	return np.inf


print(bfs())
