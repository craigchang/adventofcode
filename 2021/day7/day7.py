# https://adventofcode.com/2021/day/7


def readFile():
    with open("./day7/input.txt", "r") as f:
        return list(map(int, f.readline().strip().split(",")))


def part1():
    crabs = readFile()
    prev = float('inf')

    for pos in range(max(crabs) + 1):   
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - pos)
        if prev < fuel: # at the minimum, can no longer decrease
            break
        prev = fuel

    print(prev)
    
    # one liner solution, slow
    #print(min([sum([abs(crab - pos) for crab in crabs]) for pos in range(max(crabs) + 1)]))


def part2():
    # better, still slow
    crabs = readFile()
    prev = float('inf')

    for pos in range(max(crabs) + 1):
        fuel = 0
        for crab in crabs:
            fuel += sum([step for step in range(1, abs(crab - pos) + 1)])
        if prev < fuel: # at the minimum, can no longer decrease
            break
        prev = fuel

    print(prev)

    # one liner solution, very slow
    #print(min([sum([sum([step for step in range(1, abs(crab - pos) + 1)]) for crab in crabs]) for pos in range(max(crabs) + 1)]))


part1()
part2()