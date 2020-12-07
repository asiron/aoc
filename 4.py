
import re
from collections import defaultdict

PART1_RULES = defaultdict(lambda: lambda _: True)

PART2_RULES = {
    'byr' : lambda i: 1920 <= int(i) <= 2002 and re.match('[0-9]{4}$', i),
    'iyr' : lambda i: 2010 <= int(i) <= 2020 and re.match('[0-9]{4}$', i),
    'eyr': lambda i: 2020 <= int(i) <= 2030 and re.match('[0-9]{4}$', i),
    'hgt': lambda h: re.match(r'(1[5-8][0-9]cm)|(19[0-3]cm)|(59in)|(6[0-9]in)|(7[0-6]in)$', h),
    'hcl': lambda c: re.match(r'#[0-9abcedf]{6}$', c),
    'ecl': lambda e: re.match(r'(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)$', e),
    'pid': lambda p: re.match(r'[0-9]{9}$', p)
}

def check_rules(rules):
    with open('4.input', 'rt') as f:
        num_valid_passports = 0
        valid_fields = 0
        for line in f:

            if not line.strip():
                num_valid_passports += (valid_fields == 7)
                valid_fields = 0
                continue

            tokens = map(lambda token: token.split(':'), line.split(' '))
            for token, value in tokens:
                if token != 'cid' and rules[token](value):
                    valid_fields += 1

    return num_valid_passports + (valid_fields == 7)

def part1():
    return check_rules(PART1_RULES)

def part2():
    return check_rules(PART2_RULES)


''' Alternative solution using iterators '''
def check_rules_iter_fun(rules):
    import itertools, functools
    with open('4.input', 'rt') as f:
        # get passports
        groups = itertools.groupby(f, key=lambda l: not l.strip())
        passports = map(lambda g: g[1], filter(lambda g: not g[0], groups))

        def check_passport(lines):
            get_tokens = lambda line: map(lambda token: token.split(':'), line[:-1].split(' '))
            tokens = itertools.chain.from_iterable(map(get_tokens, lines))
            return sum(1 for token, value in tokens if token != 'cid' and rules[token](value)) == 7

        valid_passports = map(check_passport, passports)
        return sum(valid_passports)

def part1_iter_fun():
    return check_rules_iter_fun(PART1_RULES)

def part2_iter_fun():
    return check_rules_iter_fun(PART2_RULES)


if __name__ == '__main__':
    print(f'Part1: Number of valid passports: {part1()}')
    print(f'Part2: Number of valid passports: {part2()}')
    print(f'Part1A: Number of valid passports: {part1_iter_fun()}')
    print(f'Part2A: Number of valid passports: {part2_iter_fun()}')
