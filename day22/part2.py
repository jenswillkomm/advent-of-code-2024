from collections import defaultdict


input = '''1
2
3
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


sell_prices = defaultdict(int)
buyers_secret_numbers = map(int, input.splitlines())
for secret_number in buyers_secret_numbers:
	price_changes = []
	seen_sequences = set()
	
	for round in range(2000):
		new_secret_number = next_secret_number(secret_number)
		curr_price = secret_number % 10
		new_price = new_secret_number % 10
		
		price_changes.append(new_price - curr_price)
		price_changes = price_changes[-4:]
		assert(len(price_changes) <= 4)
		
		if len(price_changes) == 4 and tuple(price_changes) not in seen_sequences:
			seen_sequences.add(tuple(price_changes))
			sell_prices[tuple(price_changes)] += new_price
		
		secret_number = new_secret_number


print(max(sell_prices.values()))
