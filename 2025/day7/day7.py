# https://adventofcode.com/2025/day/7

def read_lines(filename="input.txt"):
    with open(f"2025/day7/{filename}", "r") as f:
        return [list(line.strip()) for line in f.readlines()]

def part1():
    data = read_lines()
    sx = data[0].index('S')
    queue = [(sx,0)]
    visited = set()
    visited.add((sx,0))
    result = 0

    while queue:
        x,y = queue.pop(0)
        if y+1 >= len(data):
            continue
        next = data[y+1][x]
        if next == '.':
            if (x,y+1) not in visited:
                visited.add((x,y+1))
                queue.append((x,y+1))
        elif next == '^':
            result += 1
            if (x-1,y+1) not in visited:
                visited.add((x-1,y+1))
                queue.append((x-1,y+1))
            if (x+1,y+1) not in visited:
                visited.add((x+1,y+1))
                queue.append((x+1,y+1))

    print(f"Part 1: {result}")

def part2():
    data = read_lines()
    sx = data[0].index('S')
    height = len(data)
    width = len(data[0])
    dp = [[0] * width for _ in range(height)]
    for x in range(width):
        dp[height-1][x] = 1
    for y in range(height-2, -1, -1):
        for x in range(width):
            if data[y][x] in ['S', '.', '|']:
                if y+1 < height and data[y+1][x] == '.':
                    dp[y][x] = dp[y+1][x]
                elif y+1 < height and data[y+1][x] == '^':
                    if x-1 >= 0 and x+1 < width:
                        dp[y][x] = dp[y+1][x-1] + dp[y+1][x+1]
    result = dp[0][sx]
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part1()
    part2()
