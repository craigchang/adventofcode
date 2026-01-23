# https://adventofcode.com/2016/day/1

#DIRECTIONS = ["N", "E", "S", "W"]
STEPS = ((0,1),(1,0),(0,-1),(-1,0))

def read_file(file_input):
    with open(f"2016/day1/{file_input}", "r") as f:
        return f.readline().split(", ")

def calcDirection(dir, dir_index):
    if dir == "R":
        dir_index = (dir_index + 1) % 4
    elif dir == "L":
        dir_index = (dir_index - 1) % 4
    return dir_index

def calcDistance(distance, dir_index, coords):
    x, y = coords
    xd, yd = STEPS[dir_index]
    return (x + distance * xd, y + distance * yd)

def calcPath(distance, dir_index, coords, locations=set):
    x, y = coords
    xd, yd = STEPS[dir_index]

    if xd != 0:
        for i in range(x + xd, x + distance * xd, xd):
            if (i,y) in locations:
                return True, (i,y)
            locations.add((i,y))
    if yd != 0:
        for j in range(y + yd, y + distance * yd, yd):
            if (x,j) in locations:
                return True, (x,j)
            locations.add((x,j))

    return False, calcDistance(distance, dir_index, coords)
    
def part1():
    dir_index = 0
    coords = [0,0]
    for d in read_file("input.txt"):
        d = d.strip()
        dir_index = calcDirection(d[0], dir_index)
        coords = calcDistance(int(d[1:]), dir_index, coords)
    print(abs(coords[0]) + abs(coords[1]))

def part2():
    dir_index = 0
    coords = [0,0]
    locations = {(0,0)}
    for d in read_file("input.txt"):
        d = d.strip()
        dir_index = calcDirection(d[0], dir_index)
        visited_twice, coords = calcPath(int(d[1:]), dir_index, coords, locations)
        if visited_twice:
            print(abs(coords[0]) + abs(coords[1]))
            break

part1()
part2()