import re

def count_valid_password(predicate):
    with open('2.input', 'rt') as f:
        return sum(predicate(line) for line in f)

def part1_is_valid_passwd(line):
    min_num, max_num, char, _, string = re.split('[- :]', line)
    return int(min_num) <= sum(1 for c in string if c == char) <= int(max_num)


def part2_is_valid_passwd(line):
    pos1, pos2, char, _, string = re.split('[- :]', line)
    return (string[int(pos1)-1] == char) ^ (string[int(pos2)-1] == char)

def part1():
    '''
        O(N*S) time, where N is number of lines and S is avg length of the line
        O(S) worst case space complx. where S is length of the longest line
    '''
    return count_valid_password(part1_is_valid_passwd)

def part2():
    ''' If input is already in memory,
            then time complx. is O(N), where N is number of lines
            then space is O(1) because no extra space is required
    '''

    return count_valid_password(part2_is_valid_passwd)

if __name__ == '__main__':
    print(f'Part1: {part1()}')
    print(f'Part2: {part2()}')
