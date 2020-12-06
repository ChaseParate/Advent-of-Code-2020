def toboggan_trajectory(puzzle_input):
    trees = 0
    for i, line in enumerate(puzzle_input):
        if line[(i * 3) % len(line)] == '#':
            trees += 1
    return trees


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print(toboggan_trajectory(puzzle_input))
