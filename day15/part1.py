import numpy as np


input = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
'''

# with open('input', 'r') as f:
# 	input = f.read()


directions = {
	'^': (-1, 0),
	'<': (0, -1),
	'>': (0, 1),
	'v': (1, 0)
}


def move(position, direction):
	assert(map[position] in {'@', 'O'})
	pos_next = tuple(np.add(position, direction))
	
	if map[pos_next] == 'O':
		move(pos_next, direction)
	
	if map[pos_next] == '.':
		map[position], map[pos_next] = map[pos_next], map[position]
		return pos_next
	return position


map, moves = input.split('\n\n')
map = np.array([list(row) for row in map.splitlines()])
robot = tuple(np.argwhere(map == '@')[0])

for row in moves.splitlines():
	for m in row:
		robot = move(robot, directions[m])


print(sum([100 * m + n for m, n in np.argwhere(map == 'O')]))
