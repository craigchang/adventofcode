# https://adventofcode.com/2025/day/4

ADJ = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def read_lines(filename="input.txt"):
    with open(f"2025/day4/{filename}", "r") as f:
        return [line.strip() for line in f.readlines()]

def is_within_boundary(x,dx,y,dy,col_len,row_len):
    return 0 <= x+dx and x+dx < col_len and 0 <= y+dy and y+dy < row_len

def remove_rolls(grid):
    col_len, row_len = len(grid[0]), len(grid)
    result = 0
    removed_rolls = []
    for y in range(row_len):
        for x in range(col_len):
            if grid[y][x] == '@':
                rolls = 0
                for dx,dy in ADJ:
                    if is_within_boundary(x,dx,y,dy,col_len,row_len):
                        if grid[y+dy][x+dx] == '@':
                            rolls += 1
                if rolls < 4:
                    result += 1
                    removed_rolls.append((y,x))
    for (y,x) in removed_rolls: # remove from grid
        grid[y][x] = '.'
    return result

def part1():
    print(f"Part 1: {remove_rolls([list(row) for row in read_lines()])}")

def part2():
    grid = [list(row) for row in read_lines()]
    result = 0
    while True:
        rolls = remove_rolls(grid)
        if rolls == 0:
            break
        result += rolls
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part1()
    part2()
