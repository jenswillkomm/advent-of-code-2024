input = '''2333133121414131402'''

# with open('input', 'r') as f:
# 	input = f.read().splitlines()[0]


disk_blocks = []
free_space_blocks = []


next_file_id = 0
for i, nb_blocks in enumerate(input):
	nb_blocks = int(nb_blocks)
	if i % 2 == 0:  # file
		disk_blocks.extend([next_file_id] * nb_blocks)
		next_file_id += 1
	else:  # free space
		free_space_blocks.extend(range(len(disk_blocks), len(disk_blocks) + nb_blocks))
		disk_blocks.extend(['.'] * nb_blocks)

for i in free_space_blocks:
	while disk_blocks[-1] == '.':
		disk_blocks.pop()
	
	if i > len(disk_blocks):
		break
	
	disk_blocks[i] = disk_blocks.pop()

checksum = [i * file_id for i, file_id in enumerate(disk_blocks)]


print(sum(checksum))
