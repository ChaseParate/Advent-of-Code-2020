from string import hexdigits


def part1(puzzle_input):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    valid_passports = 0
    for passport in puzzle_input:
        fields = [k for k in passport.replace('\n', ' ').split(' ')]
        keys = {f.split(':')[0] for f in fields}

        if len(required_fields.difference(keys)) == 0:
            valid_passports += 1

    return valid_passports


def part2(puzzle_input):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    
    valid_passports = 0
    for passport in puzzle_input:
        fields = [k for k in passport.replace('\n', ' ').split(' ')]
        keys = {f.split(':')[0]: f.split(':')[1] for f in fields}

        if len(required_fields.difference(keys)) != 0:
            continue
        
        valid = True
        if not 1920 <= int(keys['byr']) <= 2002:
            valid = False
        elif not 2010 <= int(keys['iyr']) <= 2020:
            valid = False
        elif not 2020 <= int(keys['eyr']) <= 2030:
            valid = False
        elif len(keys['hgt']) < 3 or not (150 <= int(keys['hgt'][:-2]) <= 193
                                          if keys['hgt'][-2:] == 'cm' else
                                          59 <= int(keys['hgt'][:-2]) <= 76):
            valid = False
        elif keys['hcl'][0] != '#' or len(keys['hcl']) != 7 or \
        not all(_ in '0123456789abcdef' for _ in keys['hcl'][1:]):
            valid = False
        elif keys['ecl'] not in \
        ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            valid = False
        elif not keys['pid'].isdigit() or len(keys['pid']) != 9:
            valid = False
        
        if valid:
            valid_passports += 1

    return valid_passports


with open('input.txt') as f:
    data = f.read()

puzzle_input = data.strip().split('\n\n')
print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
