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
diffs = [abs(x - y) for x, y in zip(sorted(lhs), sorted(rhs))]


print(sum(diffs))
