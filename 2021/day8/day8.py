# https://adventofcode.com/2021/day/8

import re

def readFile():
    # returns list of lines where each line has list of segments and list of displays
    with open("./day8/input.txt", "r") as f:
        lines = []
        for line in f:
            segs, displays = line.strip().split(" | ")
            lines.append((["".join(sorted(s)) for s in segs.split()], ["".join(sorted(d)) for d in displays.split()]))
        return lines

def deduceSegments(segments, displays):
    segmentMap = dict()

    segmentsWith5 = []
    segmentsWith6 = []

    # 1. Find 1, 4, 7, 8. Digits with unique number of segments
    for s in segments:
        lenS = len(s)
        if lenS == 2:
            segmentMap[s] = 1
            segmentMap[1] = s
        elif lenS == 4:
            segmentMap[s] = 4
            segmentMap[4] = s
        elif lenS == 3:
            segmentMap[s] = 7
            segmentMap[7] = s
        elif lenS == 7:
            segmentMap[s] = 8
            segmentMap[8] = s
        elif lenS == 5:
            segmentsWith5.append(s)
        elif lenS == 6:
            segmentsWith6.append(s)

    # 0, 6, 9 each have 6 segments
    for s in segmentsWith6:
        if set(segmentMap[4]) < set(s):
            segmentMap[9] = s
            segmentMap[s] = 9
        elif not set(segmentMap[7]) < set(s):
            segmentMap[6] = s
            segmentMap[s] = 6
        else:
            segmentMap[0] = s
            segmentMap[s] = 0

    # 2, 3, 5 each have 5 segments
    for s in segmentsWith5:
        if set(segmentMap[1]) < set(s):
            segmentMap[s] = 3
            segmentMap[3] = s
        elif len(set(s).symmetric_difference(set(segmentMap[6]))) == 1:
            segmentMap[5] = s
            segmentMap[s] = 5
        else:
            segmentMap[2] = s
            segmentMap[s] = 2
            
    return int(''.join([str(segmentMap[d]) for d in displays]))


def part1():
    lines = readFile()
    print(sum([1 for line in lines for digit in line[1] if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7]))


def part2():
    lines = readFile()
    print(sum([deduceSegments(line[0], line[1]) for line in lines]))


part1()
part2()