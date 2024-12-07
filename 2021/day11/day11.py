# https://adventofcode.com/2021/day/11


def readFile():
    with open("./day11/input.txt", "r") as f:
        return [list(map(int, list(line.strip()))) for line in f]


def part1():
    grid = readFile()
    flashes = 0
    steps = 100

    for step in range(steps):
        # add energy level by 1
        grid = [ [grid[y][x] + 1 for x in range(len(grid[0]))] for y in range(len(grid)) ]

        # if > 9, add 1 around it
        noMoreFlashes = False
        flashHistory = []
        while not noMoreFlashes:
            noMoreFlashes = True
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] > 9 and (x,y) not in flashHistory:
                        noMoreFlashes = False
                        flashHistory.append((x,y)) # keep track of octo already lit
                        for adjX, adjY in [(x-1, y-1),(x-1, y),(x-1, y+1),(x, y-1),(x, y+1),(x+1, y-1),(x+1, y),(x+1, y+1)]:
                            if adjX >= 0 and adjY >= 0 and adjX < len(grid[0]) and adjY < len(grid): # within boundary
                                grid[adjY][adjX] += 1

        # set level to 0 for any octo lit
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] > 9:
                    grid[y][x] = 0
                    flashes += 1

    print(flashes)


def part2():
    grid = readFile()
    flashes = 0
    step = 0

    while True:        
        # add energy level by 1
        grid = [ [grid[y][x] + 1 for x in range(len(grid[0]))] for y in range(len(grid)) ]

        # if > 9, add 1 around it
        noMoreFlashes = False
        flashHistory = []
        while not noMoreFlashes:
            noMoreFlashes = True
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] > 9 and (x,y) not in flashHistory:
                        noMoreFlashes = False
                        flashHistory.append((x,y)) # keep track of octo already lit
                        for adjX, adjY in [(x-1, y-1),(x-1, y),(x-1, y+1),(x, y-1),(x, y+1),(x+1, y-1),(x+1, y),(x+1, y+1)]:
                            if adjX >= 0 and adjY >= 0 and adjX < len(grid[0]) and adjY < len(grid): # within boundary
                                grid[adjY][adjX] += 1

        # set level to 0 for any octos lit
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] > 9:
                    grid[y][x] = 0
                    flashes += 1

        # check if all octos are lit
        if sum(sum(grid[y]) for y in range(len(grid))) == 0:
            print(step+1)
            break

        step += 1


part1()
part2()