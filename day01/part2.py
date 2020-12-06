def report_repair(puzzle_input):
    for i, num1 in enumerate(puzzle_input):
        for j, num2 in enumerate(puzzle_input[i+1:]):
            for k, num3 in enumerate(puzzle_input[j+1:]):
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = list(map(int, data.splitlines()))
print(report_repair(puzzle_input))
