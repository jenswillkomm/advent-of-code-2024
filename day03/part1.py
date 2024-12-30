import re


input = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

# with open('input', 'r') as f:
# 	input = f.read()


print(sum([int(m[1]) * int(m[2]) for m in re.finditer(r'mul\((\d+),(\d+)\)', input)]))
