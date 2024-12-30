import functools


input = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''

# with open('input', 'r') as f:
# 	input = f.read()


page_ordering_rules, update = input.split('\n\n')
page_ordering_rules = [(int(lhs), int(rhs)) for lhs, rhs in [rule.split('|') for rule in page_ordering_rules.splitlines()]]


def cmp_page_ordering(lhs, rhs):
	if lhs == rhs:
		return 0
	if (lhs, rhs) in page_ordering_rules:
		return -1
	return 1


update = [list(map(int, u.split(','))) for u in update.splitlines()]
middle_page_numbers = [sorted(u, key=functools.cmp_to_key(cmp_page_ordering))[len(u) // 2] for u in update if u != sorted(u, key=functools.cmp_to_key(cmp_page_ordering))]


print(sum(middle_page_numbers))
