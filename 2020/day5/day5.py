import math

def readFile():
    with open("day5/input.txt", "r") as file: # replace F, L with 0 and B, R with 1
        return [line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1").rstrip() for line in file]

def getSeatIds():
    return [ int(bp[0:7], 2) * 8 + int(bp[7:10], 2) for bp in readFile() ]

def part1():
    print(max(getSeatIds()))

def part2(seatIds):
    seatIds.sort()
    print( list(set([i for i in range(seatIds[0], seatIds[len(seatIds) - 1] + 1)]) - set(seatIds))[0] ) # find missing diff
        
part1()
part2(getSeatIds())