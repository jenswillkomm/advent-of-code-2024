import itertools


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
	return validate_safety(levels) or validate_safety(list(reversed(levels)))


def validate_safety(levels, problem_dampener = 0):
	if problem_dampener > 1:
		return False
	
	bad_levels = [not (0 < b - a < 4) for a, b in itertools.pairwise(levels)]
	
	if sum(bad_levels) <= 0:
		return True
	
	for i, v in enumerate(bad_levels):
		if not v:
			continue
		if validate_safety(levels[:i] + levels[i + 1:], problem_dampener + 1) or validate_safety(levels[:i + 1] + levels[i + 2:], problem_dampener + 1):
			return True
	return False


reports = [parse(levels) for levels in input.splitlines()]
safe_reports = list(filter(is_safe, reports))


print(len(safe_reports))
