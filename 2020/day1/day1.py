# import Timer

import sys
sys.path.append('../adventofcode2020/timer')
import Timer

def readFile():
    with open("day1/sample.txt", "r") as file:
        data = [int(x) for x in file]
    return data

def part1():
    data = readFile()

    # brute force O(n^2)
    # for i in data:
    #     for j in data:
    #         if (i + j == 2020):
    #             return i * j

    # hash solution O(n)
    vals = {}
    for i in range(len(data)):
        val = 2020 - data[i]
        if (val in vals):
            return val * data[i]
        else:
            vals[data[i]] = i

def part2():
    data = readFile()

    # brute force O(n^3)
    for i in data:
        for j in data:
            for k in data:
                if (i + j + k == 2020):
                    return i * j * k

    # hash solution O(n^2)
    vals = {}
    for i in range(len(data)):
        sum1 = 2020 - data[i]
        for j in range(len(data) - i):
            sum2 = sum1 - data[j]
            if (sum2 in vals):
                return sum2 * data[i] * data[j]
            else:
                vals[data[j]] = j



print(part1())


#print(part2())

