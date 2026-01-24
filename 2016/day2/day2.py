# https://adventofcode.com/2016/day/2

keypad = [['1','2','3'],
          ['4','5','6'],
          ['7','8','9']]

keypad2 = [['0','0','1','0','0'],
           ['0','2','3','4','0'],
           ['5','6','7','8','9'],
           ['0','A','B','C','0'],
           ['0','0','D','0','0']]

# Up, Right, Down, Left
STEPS = {
    "U": (0,-1),
    "R": (1,0),
    "D": (0,1),
    "L": (-1,0)
}

def read_lines(filename="input.txt"):
    with open(f"2016/day2/{filename}", "r") as f:
        return [line.strip() for line in f.readlines()]

def part1():
    result = ""
    x,y = (1,1)
    for l in read_lines():
        for d in l:
            xd, yd = STEPS[d]
            if x + xd >= 0 and x + xd <= 2:
                x += xd
            if y + yd >= 0 and y + yd <= 2:
                y += yd
        result += keypad[y][x]
    print(f"Part 1: {result}")

def part2():
    result = ""
    x,y = (0,2)
    for l in read_lines():
        for d in l:
            xd, yd = STEPS[d]
            if x + xd >= 0 and x + xd <= 4 and keypad2[y][x+xd] != '0':
                x += xd
            if y + yd >= 0 and y + yd <= 4 and keypad2[y+yd][x] != '0':
                y += yd
        result += keypad2[y][x]
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part1()
    part2()
