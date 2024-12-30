input = '''125 17'''

# with open('input', 'r') as f:
# 	input = f.read()


def apply_rule(number):
	if number == 0:
		return [1]
	
	n_str = str(number)
	n_len = len(n_str)
	
	if n_len % 2 == 0:
		return [int(n_str[:n_len // 2]), int(n_str[n_len // 2:])]
	
	return [2024 * number]


stones = list(map(int, input.split(' ')))
for i in range(25):
	stones = [stone for number in stones for stone in apply_rule(number)]


print(len(stones))
