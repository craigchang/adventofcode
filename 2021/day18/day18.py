# https://adventofcode.com/2021/day/18

import re
import ast


def readFile():
    with open("./day18/sample.txt", "r") as f:
        results = []
        for line in f:
            s = ast.literal_eval(line.strip())
            results.append(s)
        return results
    

def countNestedList(l, ct=0):
    if type(l) != list:
        return 0
    else:
        ct += 1
        
        if type(l[0]) == list:
            print('left')
            countNestedList(l[0], ct)
            print(l, ct)

        if len(l) == 2 and type(l[1]) == list:
            print('right')
            countNestedList(l[1], ct)
            print(l, ct)

        

        return ct


def main():
    snails = readFile()

    result = []
    for s in snails:
        if len(result) < 2:
            result.append(s)
        elif len(result) >= 2:
            result = [[result[0], result[1]]] + [s]

    print(result)
    print(countNestedList(result[0]))

    return

main()