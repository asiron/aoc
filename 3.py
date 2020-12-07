import functools

def iterate_by_jumping_n_elements(iterable, jump=1):
    yield from map(lambda ele: ele[1], filter(lambda ele: ele[0] % jump == 0, enumerate(iterable)))

def run_slope(right=1, down=1):
    with open('3.input', 'rt') as f:
        encountered_trees = 0
        current_hori_pos = 0

        for _ in range(down):
            ''' skip first N=down lines '''
            next(f)
        for line in iterate_by_jumping_n_elements(f, down):
            current_hori_pos = (current_hori_pos + right) % (len(line)-1)
            encountered_trees += (line[current_hori_pos] == '#')

        return encountered_trees

def part1():
    ''' if grid is in memory then time is O(N)
        where N is number of lines
        and space is O(1) since no extra space is required
    '''
    return run_slope(right=3, down=1)

def part2():
    ''' again if grid is in memory then time is O(N*S)
        where N is number of lines and S is number of slope runs
        and space is again O(1) since no extra space is required
    '''

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    return functools.reduce(lambda acc,slope: run_slope(*slope)*acc, slopes, 1)

if __name__ == '__main__':
    print(f'Part1: Nuber of encountered trees: {part1()}')
    print(f'Part2: Total product of encountered trees on each slope run: {part2()}')
