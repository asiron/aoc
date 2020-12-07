import re
from collections import defaultdict, deque

def get_bag_rules():
    with open('7.input', 'rt') as f:

        for line in f:
            outer_bag, inner_bags = re.match('([\w ]+) bags contain (.*)\.$', line[:-1]).groups()
            if inner_bags == 'no other bags':
                continue

            inner_bags = [re.match('(\d+) ([\w ]+?) bags?', bag).groups() for bag in inner_bags.split(', ')]
            for (n, inner_bag) in inner_bags:
                yield outer_bag, n, inner_bag

def part1():
    with open('7.input', 'rt') as f:

        adjacency_list = defaultdict(list)
        for outer_bag, _, inner_bag in get_bag_rules():
            adjacency_list[inner_bag].append(outer_bag)

        def bfs(root):
            count, visited, queue = 0, set(), deque([root])
            while len(queue) > 0:
                node = queue.pop()
                neighbours = adjacency_list[node]
                for neighbour in neighbours:
                    if not neighbour in visited:
                        queue.append(neighbour)
                        count += 1
                visited.add(node)
            return count - 1

        return bfs('shiny gold')

def part2():
    with open('7.input', 'rt') as f:

        adjacency_list = defaultdict(list)
        for outer_bag, n, inner_bag in get_bag_rules():
            adjacency_list[outer_bag].append((int(n), inner_bag))

        def dfs(root):
            neighbours = adjacency_list[root]
            if not len(neighbours):
                return 0
            return sum(n + n * dfs(neighbour) for n, neighbour in neighbours)

        return dfs('shiny gold')

if __name__ == '__main__':
    print(f'Part1: Number of bag colors that can eventually contain at least one shiny gold bag is {part1()}')
    print(f'Part2: Number of individual bags required inside 1 shiny gold bag is {part2()}')
