def part1():
    with open('13.input', 'rt') as f:
        timestamp, buses  = f.readlines()
        timestamp = int(timestamp[:-1])
        buses = [int(b) for b in buses[:-1].split(',') if b != 'x']
        wait = lambda b: (timestamp // b) * b + b - timestamp
        wait_times = map(wait, buses)
        wait_time, id = min(zip(buses, wait_times), key=lambda x: x[1])
        return wait_time * id

def part2():
    with open('13.input', 'rt') as f:
        _, buses  = f.readlines()
        buses = buses[:-1].split(',')
        time, interval = 1, 1
        for idx, bus in enumerate([int(x) if x != 'x' else 1 for x in buses]):
            while True:
                if (time + idx) % bus == 0:
                    interval *= bus
                    break
                time += interval

        return time
if __name__ == '__main__':
    print(f'Part1: {part1()}')
    print(f'Part2: {part2()}')
