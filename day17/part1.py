import re
import math


input = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
'''

# with open('input', 'r') as f:
# 	input = f.read()


initialization, program = input.split('\n\n')

registers = {}
for line in initialization.splitlines():
	m = re.match(r'Register ([ABC]): (\d+)', line)
	registers[m[1]] = int(m[2])

program = re.match(r'Program: ([0-7,]+)', program.splitlines()[0])[1].split(',')
instruction_pointer = 0
output = []

while instruction_pointer < len(program):
	opcode = program[instruction_pointer]
	operand = program[instruction_pointer + 1]
	combo_operand = int(operand)
	match operand:
		case '4':
			combo_operand = registers['A']
		case '5':
			combo_operand = registers['B']
		case '6':
			combo_operand = registers['C']
		case '7':
			assert(False)
	match opcode:
		case '0':
			registers['A'] = math.trunc(registers['A'] / math.pow(2, combo_operand))
		case '1':
			registers['B'] = registers['B'] ^ int(operand)
		case '2':
			registers['B'] = (combo_operand % 8) & 0b111
		case '3':
			if registers['A'] != 0:
				instruction_pointer = int(operand)
				continue
		case '4':
			registers['B'] = registers['B'] ^ registers['C']
		case '5':
			output.append(combo_operand % 8)
		case '6':
			registers['B'] = int(registers['A'] / math.pow(2, combo_operand))
		case '7':
			registers['C'] = int(registers['A'] / math.pow(2, combo_operand))
	instruction_pointer += 2


print(','.join(map(str, output)))
