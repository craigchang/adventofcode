# https://adventofcode.com/2021/day/2


def readFile():
    with open("./day2/input.txt", "r") as f:
        return [ command.strip().split(" ") for command in f]


def part1():
    commands = readFile()
    depth = pos = 0

    for command in commands:
        direction, units = command[0], int(command[1])

        if direction == 'forward':
            pos += units
        else:
            depth += units if direction == 'up' else -units
    
    print(abs(pos * depth))


def part2():
    commands = readFile()
    depth = pos = aim = 0

    for command in commands:
        direction, units = command[0], int(command[1])
        if direction == 'forward':
            pos += units
            depth += aim * units
        else:
            aim += units if direction == 'up' else -units
    
    print(abs(pos * depth))


part1()
part2()

