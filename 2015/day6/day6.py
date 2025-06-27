# https://adventofcode.com/2015/day/6

import re

# part 1
with open("2015/day6/input.txt") as f:
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for l in f.readlines():
        x1,y1,x2,y2 = list(map(int, re.findall("(\d+),(\d+) through (\d+),(\d+)", l.strip())[0]))
        if l.startswith("turn on"):
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y][x] = 1
        elif l.startswith("turn off"):
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y][x] = 0
        else: #toggle
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y][x] = 1 if grid[y][x] == 0 else 0

    print(sum(map(sum,grid)))

# part 2
with open("2015/day6/input.txt") as f:
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for l in f.readlines():
        x1,y1,x2,y2 = list(map(int, re.findall("(\d+),(\d+) through (\d+),(\d+)", l.strip())[0]))
        if l.startswith("turn on"):
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y][x] += 1
        elif l.startswith("turn off"):
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y][x] -= 1 if grid[y][x] > 0 else 0
        else: # toggle
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y][x] += 2

    print(sum(map(sum,grid)))