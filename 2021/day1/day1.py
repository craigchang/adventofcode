# https://adventofcode.com/2021/day/1

def readFile():
    with open("./day1/input.txt", "r") as f:
        return [int(l.strip()) for l in f]

def part1():
    depths = readFile()
    print(sum([1 for i in range(1, len(depths)) if depths[i] > depths[i-1]]))

def part2():
    depths = readFile()
    print(sum(1 for i in range(3, len(depths)) if sum(depths[i-3:i-1]) < sum(depths[i-2:i])))
    
part1()
part2()