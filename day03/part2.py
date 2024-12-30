import re


input = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

# with open('input', 'r') as f:
# 	input = f.read()


enabled_instructions = ''.join([s.split("don't()")[0] for s in input.split("do()")])


print(sum([int(m[1]) * int(m[2]) for m in re.finditer(r'mul\((\d+),(\d+)\)', enabled_instructions)]))
