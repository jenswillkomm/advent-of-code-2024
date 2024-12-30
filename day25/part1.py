import itertools
import numpy as np


input = '''#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
'''

# with open('input', 'r') as f:
# 	input = f.read()


schematics_locks = set()
schematics_keys = set()

for schematic in input.split('\n\n'):
	s = np.array([list(line) for line in schematic.splitlines()])
	heights = tuple(np.sum(s == '#', axis=0) - 1)
	
	match s[0, 0]:
		case '#':  # lock
			schematics_locks.add(heights)
		case '.':  # key
			schematics_keys.add(heights)
		case _:
			assert(False)

fitting_pairs = 0
for lock, key in itertools.product(schematics_locks, schematics_keys):
	if np.any(np.add(lock, key) > 5):
		continue
	fitting_pairs += 1


print(fitting_pairs)
