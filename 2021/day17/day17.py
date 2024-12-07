# https://adventofcode.com/2021/day/17

import re


def readFile():
    with open("./day17/input.txt", "r") as f:
        return list(map(int, re.findall("x=(\-?\d+)..(\-?\d+), y=(\-?\d+)..(\-?\d+)", f.readline())[0]))


def main():
    xMin, xMax, yMin, yMax = readFile()
    overallHighestY = 0
    numHits = 0

    for vStartY in range(yMin, abs(yMin)): # estimating y min of target area to abs(y min) of target area
        for vStartX in range(0, abs(xMax) + 1): # x range at most max x of target area
            vx, vy = vStartX, vStartY
            currX,currY,highestY = 0,0,0
            inTarget = False
            while True:
                if xMin <= currX and currX <= xMax and yMin <= currY and currY <= yMax: # in target
                    inTarget = True
                    numHits += 1
                    break
                elif currY < yMin: # if past target area, break
                    break
                currX, currY = currX + vx, currY + vy
                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1
                vy -= 1
                if highestY < currY:
                    highestY = currY
            
            if inTarget and overallHighestY < highestY: # set highest y pos in trajectory if lands on target
                overallHighestY = highestY

    print(overallHighestY)
    print(numHits)


main()