def two_sum():
    ''' Streaming approach, worst case O(N) time and memory '''
    seen = set()
    with open('1.input', 'rt') as f:
        for line in f:
            cur_number = int(line)
            if (residual := 2020 - cur_number) in seen:
                return cur_number * residual
            else:
                seen.add(cur_number)

def three_sum():
    ''' N times two_sum -> O(N*N) time and O(N) memory  '''
    with open('1.input', 'rt') as f:
        numbers = list(map(int, f.readlines()))
        for n, num in enumerate(numbers):
            seen = set()
            for cur_number in numbers[n+1:]:
                if (residual := 2020 - num - cur_number) in seen:
                    return cur_number * residual * num
                else:
                    seen.add(cur_number)

if __name__ == '__main__':
    print(f'Part1: {two_sum()}')
    print(f'Part2: naive O(N^2) {three_sum()}')
