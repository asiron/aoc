import re
import numpy as np

def part1():

    move_forward = lambda num, ship: (ship + [
        [num * np.cos(np.radians(ship[2,0]))],
        [num * np.sin(np.radians(ship[2,0]))],
        [0]
    ],)

    instruction_map = {
        'N': lambda num, ship: (ship + [[0], [num],[0]],),
        'S': lambda num, ship: (ship + [[0],[-num],[0]],),
        'E': lambda num, ship: (ship + [[num], [0],[0]],),
        'W': lambda num, ship: (ship + [[-num],[0],[0]],),
        'L': lambda num, ship: (ship + [[0],[0],[num]],),
        'R': lambda num, ship: (ship + [[0],[0],[-num]],),
        'F': move_forward
    }

    ship = np.zeros((3,1))
    ship, = navigate_ship(instruction_map, [ship])
    return np.abs(ship[:2]).sum().round()

def navigate_ship(instruction_map, state):
    with open('12.input', 'rt') as f:
        for line in f:
            ins, num = re.match('^([NSEWLRF])(\d+)$', line[:-1]).groups()
            state = instruction_map[ins](int(num), *state)
        return state

def part2():

    rotate_wp = lambda rad, wp: [
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad), np.cos(rad)]
    ] @ wp

    instruction_map = {
        'N': lambda num, wp, ship: (wp + [[0], [num]], ship),
        'S': lambda num, wp, ship: (wp + [[0],[-num]], ship),
        'E': lambda num, wp, ship: (wp + [[num], [0]], ship),
        'W': lambda num, wp, ship: (wp + [[-num],[0]], ship),
        'L': lambda num, wp, ship: (rotate_wp(np.radians(num), wp), ship),
        'R': lambda num, wp, ship: (rotate_wp(np.radians(-num), wp), ship),
        'F': lambda num, wp, ship: (wp, ship + wp * num),
    }

    wp, ship = np.array([[10, 1]]).T, np.zeros((2,1))
    wp, ship = navigate_ship(instruction_map, [wp, ship])
    return np.abs(ship[:2]).sum().round()

if __name__ == '__main__':
    print(f'Part1: Manhattan distance is {part1()}')
    print(f'Part2: Manhattan distance is {part2()}')
