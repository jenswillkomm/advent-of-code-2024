from functools import cache


input = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
'''

# with open('input', 'r') as f:
# 	input = f.read()


towel_patterns, towel_designes = input.split('\n\n')
patterns = {}
for towel_pattern in towel_patterns.split(', '):
	key = towel_pattern[0]
	if key not in patterns:
		patterns[key] = []
	patterns[key].append(towel_pattern)
for key in patterns.keys():
	patterns[key] = sorted(patterns[key], key=len, reverse=True)
towel_patterns = patterns


@cache
def is_possible(design):
	if len(design) <= 0:
		return True
	
	if design[0] not in towel_patterns:
		return False
	
	for p in towel_patterns[design[0]]:
		if len(p) > len(design):
			continue
		
		if p == design[:len(p)] and is_possible(design[len(p):]):
			return True
	return False


print(sum([is_possible(design) for design in towel_designes.splitlines()]))
