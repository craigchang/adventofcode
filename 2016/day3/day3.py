# https://adventofcode.com/2016/day/3

def read_lines(filename="input.txt"):
    with open(f"2016/day3/{filename}", "r") as f:
        return [list(map(int, line.strip().split())) for line in f.readlines()]

def isTriangle(s1, s2, s3):
    s1,s2,s3 = sorted([s1,s2,s3])
    return 1 if s1 + s2 > s3 else 0

def part1():
    result = sum([isTriangle(s[0], s[1], s[2]) for s in read_lines()])
    print(f"Part 1: {result}")

def part2():
    d = read_lines()
    result = sum([isTriangle(d[i][j], d[i+1][j], d[i+2][j]) for i in range(0, len(d), 3) for j in range(3)])
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part1()
    part2()