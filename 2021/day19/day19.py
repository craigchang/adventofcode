# https://adventofcode.com/2021/day/19

def readFile():
    with open("./day19/sample.txt", "r") as f:
        reports = []
        beacons = []
        xMin, xMax = float('inf'), -float('inf')
        yMin, yMax = float('inf'), -float('inf')
        zMin, zMax = float('inf'), -float('inf')

        for line in f:
            if line.startswith("---"):
                continue
            elif not line.strip():
                reports.append(beacons)
                beacons = []
            else:
                x,y,z = line.strip().split(",")
                x,y,z = int(x), int(y), int(z)
                if x < xMin:
                    xMin = x
                if y < yMin:
                    yMin = y
                if z < zMin:
                    zMin = z
                if x > xMax:
                    xMax = x
                if y > yMax:
                    yMax = y
                if z > zMax:
                    zMax = z

                beacons.append((int(x), int(y), int(z)))

        reports.append(beacons)

    return reports, abs(int(xMin-xMax)), abs(int(yMin-yMax)), abs(int(zMin-zMax))



faceDict = {
    'front': lambda x,y,z: (x,y,z),
    'right': lambda x,y,z: (y,-x,z),
    'left': lambda x,y,z: (-y,x,z),
    'back': lambda x,y,z: (-x,-y,z),
    'up': lambda x,y,z: (-z,y,x),
    'down': lambda x,y,z: (z,y,-x)
}


def driver():
    l = [
        (-1,-1,1),
        (-2,-2,2),
        (-3,-3,3),
        (-2,-3,1),
        (5,6,-4),
        (8,0,7)
    ]

    test = [[] for i in range(24)]
    for x,y,z in l:
        combinations = [
            (x,y,z),
            (-y,x,z),
            (-x,-y,z),
            (y,-x,z),

            (x,z,y),
            (x,z,-y),
            (x,-y,-z),
            (x,-z,y)

            (y,z,x),
            (-z,y,x),
            (-y,-z,x),
            (z,-y,x),

            (x,z,y),
            (-z,x,y),
            (-x,-z,y),
            (z,-x,y),

            (-x,-y,-z),
            (y,-x,-z),
            (x,y,-z),
            (-y,x,-z),

            (-y,-z,-x),
            (z,-y,-x),
            (y,z,-x),
            (-z,y,-x),

            (-x,-z,-y),
            (z,-x,-y),
            (x,z,-y),
            (-z,x,-y)
        ]

        i = 0
        for c in combinations:
            test[i].append(c)
            i += 1

    for i in range(24):
        print(i, test[i])
    

def main():
    reports, xRange, yRange, zRange = readFile()

    xRange = 1 if xRange == 0 else xRange
    yRange = 1 if yRange == 0 else yRange
    zRange = 1 if zRange == 0 else zRange
    
    grid = dict()
    for beacon in reports[0]:
        if beacon not in grid:
            grid[beacon] = 1

    print(grid)
    print(reports, xRange, yRange, zRange)

    for report in reports[1:]:
        for bx, by, bz in report:
            print('beacon', bx,by,bz)
            beacons = 0
            for x in range(xRange):
                for y in range(yRange):
                    for z in range(zRange):
                        if (bx + x, by + y, bz + z) in grid:
                            beacons += 1
                            print(x,y,z)
            if beacons >= 3:
                print('overlap!')


    

#main()

driver()