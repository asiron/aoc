import numpy as np

def part1():
    with open('10.input', 'rt') as f:
        numbers = [0] + list(map(lambda l: int(l[:-1]), f.readlines()))
        numbers = np.sort(np.array(numbers))
        numbers = np.diff(numbers)
        numbers = np.append(numbers, [3])
        numbers = np.unique(numbers, return_counts=True)[1]
        numbers = np.prod(numbers)
        return numbers

def part2():
    ''' DP solution
    Sort numbers to get topological order -> O(NlogN) time
    DP adds O(N) time for counting all the paths in the DAG
    '''
    with open('10.input', 'rt') as f:
        numbers = [0] + list(map(lambda l: int(l[:-1]), f.readlines()))
        numbers = sorted(numbers)
        numbers = numbers + [numbers[-1] + 3]

        paths = [0] * len(numbers)
        paths[0] = 1
        for idx, number in enumerate(numbers):
            for delta_idx in [1,2,3]:
                if (lookback := idx - delta_idx) >= 0 and (number - numbers[lookback]) <= 3:
                    paths[idx] += paths[lookback]

        return paths[-1]


if __name__ == '__main__':
    print(f'Part1: Number of 1J differences multiplied by the number of 3J differences? is {part1()}')
    print(f'Part2: Number of distinct ways to arrange the adapters is {part2()}')
