# https://adventofcode.com/2025/day/6

from functools import reduce

def read_lines(filename="input.txt") -> list[str]:
    with open(f"2025/day6/{filename}", "r") as f:
        return [line.strip("\n") for line in f.readlines()]
    
def mult(iterable):
    return reduce(lambda x,y: x*y, iterable)

def part1():
    data = read_lines()
    nums = [list(map(int, row.strip().split())) for row in data[:-1]]
    ops = data[-1].strip().split()
    result = 0
    for x in range(len(nums[0])):
        col = [nums[y][x] for y in range(len(nums))]
        result += sum(col) if ops[x] == '+' else mult(col)
    print(f"Part 1: {result}")

def part2():
    data = read_lines()
    nums = [list(row) for row in data[:-1]]
    ops = data[-1].strip().split()
    result = 0
    op_index = 0
    num_list = []
    for x in range(len(nums[0])):
        col = [nums[y][x] for y in range(len(nums))]
        if col.count(" ") != len(col): # nums to construct
            num_list.append(int("".join(col)))
        if col.count(" ") == len(col) or x == len(nums[0])-1: # empty col or EOL
            result += sum(num_list) if ops[op_index] == '+' else mult(num_list)
            num_list = []
            op_index += 1
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part1()
    part2()