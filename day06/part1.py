def custom_customs(puzzle_input):
    sum_counts = 0

    for line in puzzle_input:
        questions = set(char for char in line if char != '\n')
        sum_counts += len(questions)

    return sum_counts


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = data.split('\n\n')
print(custom_customs(puzzle_input))
