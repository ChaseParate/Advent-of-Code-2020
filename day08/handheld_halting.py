def part1(puzzle_input):
    instructions_done = []
    pc = 0
    
    acc = 0
    while pc not in instructions_done:
        instructions_done.append(pc)

        instruction = puzzle_input[pc]
        opcode, argument = instruction.split()
        
        if opcode == 'acc':
            acc += int(argument)
        elif opcode == 'jmp':
            pc += int(argument)
            continue
        pc += 1

    return acc


def part2(puzzle_input):
    for i, line in enumerate(puzzle_input):
        if line.startswith('jmp') or line.startswith('nop'):
            new_program = puzzle_input.copy()
            if line.startswith('jmp'):
                new_program[i] = 'nop' + new_program[i][3:]
            else:
                new_program[i] = 'jmp' + new_program[i][3:]

            out = execute_program(new_program)
            if out:
                return out


def execute_program(program):
    instructions_done = []
    pc = 0
    
    acc = 0
    while pc not in instructions_done:
        instructions_done.append(pc)

        if pc >= len(program):
            return acc
        
        opcode, argument = program[pc].split()
        
        if opcode == 'acc':
            acc += int(argument)
        elif opcode == 'jmp':
            pc += int(argument)
            continue
        pc += 1

    return False


with open('input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
