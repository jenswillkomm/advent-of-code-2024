input = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''

# with open('input', 'r') as f:
# 	input = f.read()


def possible_values(numbers):
	assert len(numbers) > 0
	if len(numbers) == 1:
		return {numbers[0]}
	
	result = set()
	for possible_value in possible_values(numbers[:-1]):
		result.add(possible_value + numbers[-1])
		result.add(possible_value * numbers[-1])
	return result


equations = [equation.split(': ') for equation in input.splitlines()]
equations = [(int(test_value), list(map(int, numbers.split(' ')))) for test_value, numbers in equations]


print(sum([test_value for test_value, numbers in equations if test_value in possible_values(numbers)]))
