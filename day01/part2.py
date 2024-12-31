import re
import numpy as np


input = '''3   4
4   3
2   5
1   3
3   9
3   3
'''

# with open('input', 'r') as f:
# 	input = f.read()


def parse(s):
	m = re.match(r'(\d+)   (\d+)', s)
	return int(m.group(1)), int(m.group(2))


columns = np.array([parse(s) for s in input.splitlines()])
lhs = columns[:,0]
rhs = columns[:,1]
lhs_similarity_summands = [x * (rhs == x).sum() for x in lhs]


print(sum(lhs_similarity_summands))
