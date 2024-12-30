input = '''1
10
100
2024
'''

# with open('input', 'r') as f:
# 	input = f.read()


def mix(a, b):
	return a ^ b


def prune(a):
	return a % 16777216


def next_secret_number(secret_number):
	result = prune(mix(secret_number * 64, secret_number))
	result = prune(mix(result // 32, result))
	result = prune(mix(result * 2048, result))
	return result


buyers_secret_numbers = map(int, input.splitlines())

for round in range(2000):
	buyers_secret_numbers = map(next_secret_number, buyers_secret_numbers)


print(sum(buyers_secret_numbers))
