from itertools import product, count, takewhile
import numpy as np

def adjecent_neighbours(grid, cell, n, m):
    for dx, dy in product(*(range(x-1, x+2) for x in cell)):
        if (dx, dy) != cell and 0 <= dx < n and 0 <= dy < m:
            yield (dx, dy)

def first_chair_in_sight_neighbours(grid, cell, n, m):
    dirs = (dir for dir in product([-1, 0, 1], [-1, 0, 1]) if dir != (0,0))
    for dir in dirs:
        look_in_dir = zip(*[count(w+step, step) for w, step in zip(cell, dir)])
        look_in_dir = takewhile(lambda dxdy: 0<=dxdy[0]<n and 0<=dxdy[1]<m, look_in_dir)
        for dx,dy in look_in_dir:
            if grid[dx,dy] in ('#', 'L'):
                yield (dx, dy)
                break


def game_of_seats(seat_selection, at_least_N_occupied_seat):

    with open('11.input', 'rt') as f:
        grid = np.array([list(line[:-1]) for line in f])
        N, M = grid.shape
        while True:
            changed = False
            new_grid = grid.copy()
            for ij in product(range(N), range(M)):
                around_matching = (grid[neigh] == grid[ij]
                                   for neigh in seat_selection(grid, ij, N, M)
                                   if grid[neigh] != '.')

                if grid[ij] == 'L' and all(around_matching):
                    new_grid[ij] = '#'
                    changed = True
                elif grid[ij] == '#' and sum(around_matching) >= at_least_N_occupied_seat:
                    new_grid[ij] = 'L'
                    changed = True

            grid = new_grid
            if not changed:
                break

        return (grid == '#').sum().sum()

def part1():
    return game_of_seats(adjecent_neighbours, 4)

def part2():
    return game_of_seats(first_chair_in_sight_neighbours, 5)

if __name__ == '__main__':
    print(f'Part1: Number of occupied seat at the end is {part1()}')
    print(f'Part2: Number of occupied seat at the end is {part2()}')
