# https://adventofcode.com/2021/day/12

from collections import defaultdict


def readFile():
    with open("./day12/input.txt", "r") as f:
        caves = defaultdict(lambda:[])
        for line in f:
            a,b = line.strip().split("-")
            if a == "start" or b == "end": # one way, start -> x or x -> end
                caves[a].append(b)
            elif b == "start" or a == "end": # one way, x -> start or end -> x
                caves[b].append(a)
            else: # two way
                caves[a].append(b)
                caves[b].append(a)
        for a,b in caves.items():
            b.sort()
        return caves


def findPaths(caves, target, visited=[]):
    paths = 0

    if target == "end":
        return 1
    else:
        for cave in caves[target]:
            if cave in visited:
                continue
            if cave.islower() and cave != "end":
                visited.append(cave)
            paths += findPaths(caves, cave, visited)
        if target in visited:
            visited.remove(target)
            
    return paths


def findPaths2(caves, target, visited=defaultdict(lambda: 0)):
    paths = 0

    if target == "end":
        return 1
    else:
        for cave in caves[target]:
            if visited[cave] >= 1 and 2 in visited.values(): 
                continue # if current cave visited at least once and any cave visited twice, skip
            if cave.islower() and cave != "end":
                visited[cave] += 1
            paths += findPaths2(caves, cave, visited)
        if target in visited.keys():
            visited[target] -= 1

    return paths


def part1():
    caves = readFile()
    print(findPaths(caves, "start"))


def part2():
    caves = readFile()
    print(findPaths2(caves, "start"))


part1()
part2()