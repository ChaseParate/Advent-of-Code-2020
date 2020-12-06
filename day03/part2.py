def get_tree_count(slope, slope_x, slope_y):
    trees = 0
    for i, line in enumerate(slope[::slope_y]):
        if line[(i * slope_x) % len(line)] == '#':
            trees += 1
    return trees


def toboggan_trajectory(puzzle_input):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

    product = 1
    for slope in slopes:
        product *= get_tree_count(puzzle_input, *slope)

    return product


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print(toboggan_trajectory(puzzle_input))
