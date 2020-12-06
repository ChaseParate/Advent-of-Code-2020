def passport_processing(puzzle_input):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    valid_passports = 0
    for passport in puzzle_input:
        fields = [k for k in passport.replace('\n', ' ').split(' ')]
        keys = {f.split(':')[0] for f in fields}

        if len(required_fields.difference(keys)) == 0:
            valid_passports += 1

    return valid_passports


with open('puzzle_input.txt') as f:
    data = f.read()

puzzle_input = data.split('\n\n')
print(passport_processing(puzzle_input))
