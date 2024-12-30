from functools import cache


input = '''125 17'''

# with open('input', 'r') as f:
# 	input = f.read()


@cache
def apply_rule(number, nb_blinks):
	if nb_blinks <= 0:
		return 1
	
	if number == 0:
		return apply_rule(1, nb_blinks - 1)
	
	n_str = str(number)
	n_len = len(n_str)
	
	if n_len % 2 == 0:
		return apply_rule(int(n_str[:n_len // 2]), nb_blinks - 1) + apply_rule(int(n_str[n_len // 2:]), nb_blinks - 1)
	
	return apply_rule(number * 2024, nb_blinks - 1)


stones = list(map(int, input.split(' ')))


print(sum([apply_rule(stone, 75) for stone in stones]))
