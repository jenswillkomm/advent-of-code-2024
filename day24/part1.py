import re


input = '''x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
'''

# with open('input', 'r') as f:
# 	input = f.read()


initial_values, wiring = input.split('\n\n')

wire_values = {}
for line in initial_values.splitlines():
	m = re.match(r'([xy]\d{2}): ([01])', line)
	wire_values[m[1]] = int(m[2])

operations = set(wiring.splitlines())

while operations:
	for op in operations.copy():
		m = re.match(r'([a-z0-9]{3}) (AND|OR|XOR) ([a-z0-9]{3}) -> ([a-z0-9]{3})', op)
		
		if m[1] not in wire_values or m[3] not in wire_values:
			continue
		
		match m[2]:
			case 'AND':
				wire_values[m[4]] = wire_values[m[1]] & wire_values[m[3]]
			case 'OR':
				wire_values[m[4]] = wire_values[m[1]] | wire_values[m[3]]
			case 'XOR':
				wire_values[m[4]] = wire_values[m[1]] ^ wire_values[m[3]]
		operations.remove(op)


print(
	int(''.join(map(str, [e[1] for e in sorted([e for e in wire_values.items() if e[0][0] == 'z'], key=lambda e: e[0], reverse=True)])), 2)
)
