import builtins
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

# with open('15/input', 'r') as f:
# 	input = f.read()


directions = {
	'^': (-1, 0),
	'<': (0, -1),
	'>': (0, 1),
	'v': (1, 0)
}


def widen(tile):
	match tile:
		case '#':
			return '##'
		case 'O':
			return '[]'
		case '.':
			return '..'
		case '@':
			return '@.'
		case _:
			assert(False)
	return '..'


def get_neighbor(position):
	assert(map[position] in {'[', ']'})
	neighbor = position
	if map[position] == '[':
		neighbor = tuple(np.add(position, directions['>']))
	elif map[position] == ']':
		neighbor = tuple(np.add(position, directions['<']))
	assert(neighbor != position)
	return neighbor


def is_movable(position, direction):
	assert(map[position] in {'@', '[', ']'})
	pos_next = tuple(np.add(position, direction))
	
	if map[pos_next] == '.':
		return True
	
	if map[pos_next] == '#':
		return False
	
	assert(map[pos_next] in {'[', ']'})
	if direction in {directions['<'], directions['>']}:
		return is_movable(pos_next, direction)
	
	return is_movable(pos_next, direction) and is_movable(get_neighbor(pos_next), direction)


def move(position, direction):
	assert(map[position] in {'@', '[', ']'})
	pos_next = tuple(np.add(position, direction))
	
	if map[pos_next] in {'[', ']'}:
		if direction in {directions['^'], directions['v']}:
			neighbor = get_neighbor(pos_next)
			if is_movable(pos_next, direction) and is_movable(neighbor, direction):
				move(pos_next, direction)
				move(neighbor, direction)
		else:
			if is_movable(pos_next, direction):
				move(pos_next, direction)
	
	if map[pos_next] == '.':
		map[position], map[pos_next] = map[pos_next], map[position]
		return pos_next
	return position


map, moves = input.split('\n\n')
map = np.array([list(''.join(builtins.map(widen, row))) for row in map.splitlines()])
robot = tuple(np.argwhere(map == '@')[0])

for row in moves.splitlines():
	for m in row:
		robot = move(robot, directions[m])


print(sum([100 * m + n for m, n in np.argwhere(map == '[')]))
