import itertools
from numpy import sign


input = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''

# with open('input', 'r') as f:
# 	input = f.read()


def parse(s):
	return list(map(int, s.split(' ')))


def is_safe(levels):
	increasing = [a - b for a, b in itertools.pairwise(levels)]
	
	if sum(1 for e in increasing if abs(e) < 1 or abs(e) > 3) > 0:
		return False
	
	if sum(1 for e in increasing if sign(e) != sign(increasing[0])) > 0:
		return False
	
	return True


reports = [parse(levels) for levels in input.splitlines()]
safe_reports = list(filter(is_safe, reports))


print(len(safe_reports))
