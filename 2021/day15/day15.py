# https://adventofcode.com/2021/day/15

import math


def readFile():
    with open("./day15/input.txt", "r") as f:
        return [list(map(int,list(line.strip()))) for line in f]


def printVertices(vertices, lenX, lenY):
    print()
    for y in range(lenY):
        for x in range(lenX):
            print(vertices[(x,y)], end=' ')
        print()
                

def dijkstras(chitons, startV):
    lenX = len(chitons[0])
    lenY = len(chitons)
    vertices = {}
    visited = {}

    # init vertices and visited
    for y in range(lenY):
        for x in range(lenX):
            vertices[(x,y)] = math.inf
            visited[(x,y)] = {}
            for adjX,adjY in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if adjX >= 0 and adjX < lenX and adjY >= 0 and adjY < lenY:
                    visited[(x,y)][(adjX,adjY)] = False

    vertices[startV] = 0
    adjList = [startV]
    while True:
        if len(adjList) == 0:
            break
        temp = []
        for curr in adjList:
            for adj in visited[curr]:
                x,y = adj
                if not visited[curr][adj]:
                    visited[curr][adj] = True
                    visited[adj][curr] = True
                    if vertices[curr] + chitons[y][x] < vertices[adj]:
                        vertices[adj] = vertices[curr] + chitons[y][x]
                    temp.append((x,y))
        adjList = temp.copy()

    print(vertices[(lenX-1,lenY-1)])


def part1():
    chitons = readFile()
    dijkstras(chitons, (0,0))


def part2():
    chitons = readFile()
    lenX = len(chitons[0])
    lenY = len(chitons)

    newChitons = []
    for y in range(len(chitons)):
        chitonsRow = []
        for i in range(0,5):
            chitonsRow += [((chitons[y][x] + i - 9) if chitons[y][x] + i > 9 else chitons[y][x] + i) for x in range(len(chitons[0]))]
        newChitons.append(chitonsRow)

    for tile in range(0,4):
        temp = []
        for y in range(tile * lenY, len(newChitons)):
            temp.append([1 if newChitons[y][x] == 9 else newChitons[y][x] + 1 for x in range(len(newChitons[0]))])
        newChitons += temp

    dijkstras(newChitons, (0,0)) # real answer off by a few, need to look into it more


part1()
part2()