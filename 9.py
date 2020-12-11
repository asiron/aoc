def part1():
    ''' O(25N) = O(N) time and O(1) extra space (excluding input seq)'''
    with open('9.input', 'rt') as f:
        numbers = [int(line[:-1]) for line in f]
        for i, two_sum in enumerate(numbers[25:]):
            seen = set()
            for num in numbers[i:i+25]:
                if (residual := two_sum - num) in seen:
                    break
                seen.add(num)
            else:
                return i+25, two_sum

def part2():
    with open('9.input', 'rt') as f:
        numbers = [int(line[:-1]) for line in f]
        failed_idx, failed_two_sum = part1()
        sequence = numbers[:failed_idx]
        start_idx, end_idx = 0, 1
        current_sum = sequence[start_idx] + sequence[end_idx]
        while start_idx < failed_idx:
            if current_sum < failed_two_sum:
                end_idx += 1
                current_sum += sequence[end_idx]
            elif current_sum > failed_two_sum:
                current_sum -= sequence[start_idx]
                start_idx += 1
            else:
                range = numbers[start_idx:end_idx+1]
                return min(range) + max(range)


if __name__ == '__main__':
    print(f'Part1: First number that does not have 2 previous numbers summing up to it is {part1()[1]}')
    print(f'Part2: Sum of min and max of the contigous array that sums up to fault sum from part1 is {part2()}')
