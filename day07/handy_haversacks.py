import re


def part1(puzzle_input):
    bags = {}
    for bag in puzzle_input:
        bag_type, contained_bags = bag.split(' bags contain ')
        contained_bags = 'no other' if len(contained_bags) == 0 else \
            re.findall(r'\d (\w+ \w+)', contained_bags)

        bags[bag_type] = contained_bags

    num_bags = 0
    for bag_contents in bags.values():
        if bags_containing_shiny_gold_bag(bags, bag_contents):
            num_bags += 1
    return num_bags


def part2(puzzle_input):
    bags = {}
    for bag in puzzle_input:
        bag_type, contained_bags = bag.split(' bags contain ')
        contained_bags = 'no other' if len(contained_bags) == 0 else \
            re.findall(r'(\d \w+ \w+)', contained_bags)

        bags[bag_type] = []
        for contained_bag in contained_bags:
            count = int(contained_bag[:2])
            for i in range(count):
                bags[bag_type].append(contained_bag[2:])

    return bags_needed_for_shiny_gold_bag(bags, bags['shiny gold'])


def bags_containing_shiny_gold_bag(bags, bag_contents):
    if 'shiny gold' in bag_contents:
        return True
    elif 'no other' in bag_contents:
        return False
    else:
        return any(bags_containing_shiny_gold_bag(bags, bags[inner_bag])
                   for inner_bag in bag_contents)


def bags_needed_for_shiny_gold_bag(bags, bag_contents):
    if 'no other' in bag_contents:
        return 0
    else:
        return len(bag_contents) + sum(bags_needed_for_shiny_gold_bag(
            bags, bags[inner_bag]) for inner_bag in bag_contents)


with open('input.txt') as f:
    data = f.read()

puzzle_input = data.splitlines()
print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))
