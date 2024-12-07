# https://adventofcode.com/2021/day/13

import re

def readFile():
    with open("./day13/input.txt", "r") as f:
        dots = []
        folds = []

        for line in f: # get dots
            if not line.strip(): # skip empty line
                break
            dots.append(list(map(int, line.strip().split(','))))

        for line in f: # get folds
            tokens = re.search("fold along (x|y)=(\d+)", line.strip())
            folds.append((tokens[1], int(tokens[2])))

    return dots, folds


def main():
    dots, folds = readFile()
    lenX, lenY = max([ x for x,y in dots ]) + 1, max([ y for x,y in dots ]) + 1
    grid = [ ['.'] * lenX for y in range(lenY) ]

    for x,y in dots:
        grid[y][x] = '#'

    part1 = True
    for dir, line in folds:
        if dir == 'y':
            for y in range(line + 1, lenY):
                for x in range(lenX):
                    if grid[y][x] == '#':
                        newLine = line - (y-line) # get new y-axis position for dots
                        if newLine >= 0 and newLine <= lenY - 1:
                            grid[newLine][x] = '#'
            for y in range(line, lenY): # trim grid
                del grid[line]
            lenY = len(grid)
        elif dir == 'x':
            for x in range(line + 1, lenX):
                for y in range(lenY):
                    if grid[y][x] == '#':
                        newLine = line - (x-line) # get new x-axis position for dots
                        if newLine >= 0 and newLine <= lenX - 1:
                            grid[y][newLine] = '#'
            for y in range(lenY):
                for x in range(line, lenX):
                    del grid[y][line]
            lenX = len(grid[0])

        
        if part1: # for part 1
            print(sum([1 for y in range(lenY) for x in range(lenX) if grid[y][x] == '#']))
            part1 = False

    # part 2
    for line in grid: # display code
        print(line)


main()