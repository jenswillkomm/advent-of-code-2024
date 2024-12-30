import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import label


input = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
'''

# with open('input', 'r') as f:
# 	input = f.read()


map = np.array([list(line) for line in input.splitlines()])


def price(plant_type):
	result = 0
	map_plant_type, nbRegions = label(map == plant_type)
	for region_label in range(1, nbRegions + 1):
		region = map_plant_type == region_label
		area = np.sum(region)
		nbSides = np.sum(np.abs(convolve2d(region, [[1, -1], [-1, 1]])))
		result += area * nbSides
	return result


print(sum([price(plant_type) for plant_type in np.unique(map)]))
