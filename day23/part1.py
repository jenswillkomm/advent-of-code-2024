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

clique = set()
for vertex in V:
	edges = [e for e in E if e[0] == vertex or e[1] == vertex]
	if len(edges) < 2:
		continue
	
	neighbor_vertices = set([v for edge in edges for v in edge]) - {vertex}
	neighbor_edges = [e for e in E if e[0] in neighbor_vertices and e[1] in neighbor_vertices]
	for e in neighbor_edges:
		if vertex[0] == 't' or e[0][0] == 't' or e[1][0] == 't':
			clique.add(tuple(sorted([vertex, e[0], e[1]])))


print(len(clique))
