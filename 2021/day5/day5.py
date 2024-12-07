# https://adventofcode.com/2021/day/5

from collections import defaultdict

def readFile():
    with open("./day5/input.txt", "r") as f:
        lines = []
        for line in f:
            p1, p2 = line.strip().split(" -> ")
            lines.append( (list(map(int, p1.split(","))), list(map(int, p2.split(",")))) )
        return lines


def part1():
    lines = readFile()
    ventsMap = defaultdict(lambda: 0)

    for line in lines:
        [x1, y1], [x2, y2] = line
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2) + 1):
                ventsMap[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2) + 1):
                ventsMap[(x, y1)] += 1

    print(sum([1 for k,v in ventsMap.items() if v > 1]))


def part2():
    lines = readFile()
    ventsMap = defaultdict(lambda: 0)

    for line in lines:
        [x1, y1], [x2, y2] = line
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2) + 1):
                ventsMap[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2) + 1):
                ventsMap[(x, y1)] += 1
        elif abs((y2-y1)/(x2-x1)) == 1:
            rangeY = range(y1, y2 - 1, -1) if y1 > y2 else range(y1, y2 + 1, 1)
            rangeX = range(x1, x2 - 1, -1) if x1 > x2 else range(x1, x2 + 1, 1)
            
            for x,y in zip(rangeX, rangeY):
                ventsMap[(x, y)] += 1

    print(sum([1 for k,v in ventsMap.items() if v > 1]))

part1()
part2()