def get_seat_positions():
    with open('5.input', 'rt') as f:
        for line in f:
            row = int(line[:7].replace('F', '0').replace('B', '1'), 2)
            col = int(line[7:].replace('L', '0').replace('R', '1'), 2)
            yield (row, col)


def part1():
    return max(map(lambda x: x[0]*8+x[1], get_seat_positions()))

def part2():
    seat_map = [[False for _ in range(8)] for _ in range(128)]
    for row, col in get_seat_positions():
        seat_map[row][col] = True
    for row in range(2,126):
        for col in range(8):
            if seat_map[row][col] == False and seat_map[row+1][col] == True and seat_map[row-1][col] == True:
                return row * 8 + col

if __name__ == '__main__':
    print(f'Part1: Highest seat ID is {part1()}')
    print(f'Part2: Your seat is {part2()}')
