def part1():
    with open('8.input', 'rt') as f:
        instructions = dict(enumerate(map(lambda l: [l[:-1], False], f.readlines())))
        pc, acc = 0, 0
        while True:
            ins, _ = instructions[pc]
            code, delta = ins.split(' ')
            if code == 'acc':
                acc += int(delta)

            instructions[pc][1] = True

            pc += (1 if code in ('acc', 'nop') else int(delta))
            if instructions[pc][1] == True:
                return acc

def part2():
    with open('8.input', 'rt') as f:
        instructions = dict(enumerate(map(lambda l: l[:-1].split(' '), f.readlines())))

        visited = set()
        def dfs(node, used_fix):

            if node in visited:
                return 0, 'LOOP'

            if node == len(instructions):
                return 0, 'END'

            visited.add(node)

            code, delta = instructions[node]
            delta = int(delta)

            if code == 'acc':
                acc, status = dfs(node+1, used_fix)
                return acc+delta, status

            elif code == 'jmp' and used_fix:
                return dfs(node+delta, True)

            elif code == 'nop' and used_fix:
                return dfs(node+1, True)

            elif code == 'jmp' and not used_fix:
                left = dfs(node+delta, False)
                right = dfs(node+1, True)
                return left if left[1] == 'END' else right

            elif code == 'nop' and not used_fix:
                left = dfs(node+1, False)
                right = dfs(node+delta, True)
                return left if left[1] == 'END' else right

        return dfs(0, False)[0]


if __name__ == '__main__':
    print(f'Part1: Accumulator before reaching cycle was {part1()}')
    print(f'Part2: Accumulator after program terminated with the fix was {part2()}')
