# https://adventofcode.com/2021/day/9

def readFile():
    with open("./day9/input.txt", "r") as f:
        return [line.strip() for line in f]


def padLines(lines):
    lines = ['9' * len(lines[0])] + lines + ['9' * len(lines[0])]
    for i in range(len(lines)):
        lines[i] = '9' + lines[i] + '9'
    return lines


def part1():
    lines = padLines(readFile())

    lowPoints = []
    lowPointCoords = []
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[0]) - 1):
            curr = int(lines[y][x])
            if curr < int(lines[y-1][x]) and curr < int(lines[y+1][x]) and curr < int(lines[y][x-1]) and curr < int(lines[y][x+1]):
                lowPoints.append(curr)
                lowPointCoords.append((x,y))

    print(sum([pt+1 for pt in lowPoints]))
    return lowPointCoords


def part2(lowPointCoords):
    lines = padLines(readFile())

    basinAreas = []
    for lowPoint in lowPointCoords:
        basinStack = [lowPoint] # checks for each point in the basin
        basinPoints = [lowPoint] # remembers which points have already been calculated
        basinArea = 0
        while len(basinStack) != 0:
            currX, currY = basinStack.pop()
            basinArea += 1
            for x,y in [(currX-1,currY), (currX+1,currY), (currX,currY-1), (currX,currY+1)]:
                if int(lines[y][x]) < 9 and (x,y) not in basinPoints:
                    basinStack.append((x, y))
                    basinPoints.append((x, y))
        basinAreas.append(basinArea)

    basinAreas.sort()
    print(basinAreas[-1] * basinAreas[-2] * basinAreas[-3])


part2(part1())