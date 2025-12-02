# https://adventofcode.com/2025/day/2

import regex as re

def read_input(filename="input.txt"):
    with open(f"2025/day2/{filename}", "r") as f:
        return f.read().strip()

def part1():
    ranges = read_input().split(",")
    result = 0
    for r in ranges:
        firstID, lastID = r.split("-")
        for id in range(int(firstID), int(lastID)+1):
            if re.match(r"^(\d+)\1$", str(id)):
                result += id
    print(f"Part 1: {result}")

def part2():
    ranges = read_input().split(",")
    result = 0
    for r in ranges:
        firstID, lastID = r.split("-")
        for id in range(int(firstID), int(lastID)+1):
            if re.match(r"^(\d+)\1+$", str(id)):
                result += id
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part1()
    part2()