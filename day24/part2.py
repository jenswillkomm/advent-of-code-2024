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

output_swapped = set()
source_gate = {}

for op in wiring.splitlines():
	m = re.match(r'([a-z0-9]{3}) (AND|OR|XOR) ([a-z0-9]{3}) -> ([a-z0-9]{3})', op)
	
	# plausibility check of a Ripple-carry adder
	if not (m[2] == 'AND' and m[1][1:] == '00' and m[3][1:] == '00'):  # LSB is a half adder
		source_gate[m[4]] = m[2]
	
	if m[4][0] == 'z' and m[2] != 'XOR' and m[4] != 'z45':  # MSB comes from the carry block
		output_swapped.add(m[4])
	if m[2] == 'XOR':
		if m[1][0] not in {'x', 'y', 'z'} and m[3][0] not in {'x', 'y', 'z'} and m[4][0] not in {'x', 'y', 'z'}:
			output_swapped.add(m[4])
		if m[1] in source_gate and source_gate[m[1]] == 'AND':
			output_swapped.add(m[1])
		if m[3] in source_gate and source_gate[m[3]] == 'AND':
			output_swapped.add(m[3])
	if m[2] == 'OR':
		if m[1] in source_gate and source_gate[m[1]] != 'AND':
			output_swapped.add(m[1])
		if m[3] in source_gate and source_gate[m[3]] != 'AND':
			output_swapped.add(m[3])


print(','.join(sorted(output_swapped)))
