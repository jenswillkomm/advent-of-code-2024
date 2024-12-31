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
		free_space_blocks.append(len(disk_blocks))
		disk_blocks.extend(['.'] * nb_blocks)

for file_id in reversed(range(next_file_id)):
	file_size = disk_blocks.count(file_id)
	file_location = disk_blocks.index(file_id)
	
	target_location = 0
	while disk_blocks[target_location:target_location + file_size].count('.') != file_size and target_location < file_location:
		target_location += 1
	if target_location >= file_location:
		continue
	
	disk_blocks[target_location:target_location + file_size] = [file_id] * file_size
	disk_blocks[file_location:file_location + file_size] = ['.'] * file_size

checksum = [i * file_id for i, file_id in enumerate(disk_blocks) if file_id != '.']


print(sum(checksum))
