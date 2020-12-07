import itertools, functools, string

def part1():
    with open('6.input', 'rt') as f:

        count = 0
        questions = set()
        for line in f:

            if not line.strip():
                count += len(questions)
                questions = set()
                continue

            questions |= set(list(line[:-1]))

        return count + len(questions)


def part2():
    with open('6.input', 'rt') as f:

        count = 0
        questions = set(list(string.ascii_lowercase))
        for line in f:

            if not line.strip():
                count += len(questions)
                questions = set(list(string.ascii_lowercase))
                continue

            questions &= set(list(line[:-1]))

        return count + len(questions)

''' Alternative solution using iterators '''
def iter_fun(fun, init):
    with open('6.input', 'rt') as f:

        def sum_of_questions(g):
            stripped_new_lines = map(lambda line: line[:-1], g)
            return len(functools.reduce(fun, stripped_new_lines, init))

        groups = itertools.groupby(f, key=lambda x: not x.strip())
        filtered = map(lambda g: g[1], filter(lambda g: not g[0], groups))
        questions_per_group = map(lambda g: sum_of_questions(g), filtered)

        return sum(questions_per_group)

def part1_iter_fun():
    return iter_fun(lambda acc, person: acc | set(person), set())

def part2_iter_fun():
    return iter_fun(lambda acc, person: acc & set(person), set(string.ascii_lowercase))

if __name__ == '__main__':
    print(f'Part1: Sum of the counts is {part1()}')
    print(f'Part2: Sum of the counts is {part2()}')
    print(f'Part1A: Sum of the counts is {part1_iter_fun()}')
    print(f'Part2A: Sum of the counts is {part2_iter_fun()}')
