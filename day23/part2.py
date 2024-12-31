import re


input = '''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
'''

# with open('input', 'r') as f:
# 	input = f.read()


V = set()
E = set()
for line in input.splitlines():
	m = re.match(r'([a-z]{2})-([a-z]{2})', line)
	V |= {m[1], m[2]}
	E.add((m[1], m[2]))


def BronKerbosch(R, P, X):
	if len(P) <= 0 and len(X) <= 0:
		return [R]
	
	result = []
	for v in P.copy():
		N_v = set([v for e in [e for e in E if e[0] == v or e[1] == v] for v in e]) - {v}
		cliques = BronKerbosch(R | {v}, P & N_v, X & N_v)
		if len(cliques) > 0:
			result.extend(cliques)
		P.remove(v)
		X.add(v)
	
	return result


cliques = BronKerbosch(set(), V, set())
maximal_clique = sorted(cliques, key=len, reverse=True)[0]
password = ','.join(sorted(maximal_clique))


print(password)
