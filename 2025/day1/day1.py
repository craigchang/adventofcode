# https://adventofcode.com/2025/day/1

import regex as re

def read_lines(filename="input.txt"):
    with open(f"2025/day1/{filename}", "r") as f:
        return [line.strip() for line in f.readlines()]

def calc_distance(data):
    rotation, distance = re.findall(r"([LR])(\d+)", data)[0]
    distance = int(distance)
    return distance if rotation == "R" else -distance

def part1():
    data = read_lines("input.txt")
    old_pos = 50
    result = 0
    for r in data:
        old_pos += calc_distance(r)
        while old_pos < 0: # each iter is one revolution
            old_pos += 100
        while old_pos >= 100:
            old_pos -= 100
        if old_pos == 0:
            result += 1        
    print(f"Part 1: {result}")
    return result

def part2():
    data = read_lines()
    curr_pos = 50
    final_pos = 50
    result = 0
    for r in data:
        final_pos += calc_distance(r)
        while final_pos < 0:  # each iter is one revolution
            if -99 <= final_pos and final_pos < 0: # compare final position to original position
                final_pos += 100
                if curr_pos > 0:
                    result += 1
            else:
                final_pos += 100
                result += 1
                
        while final_pos > 100:
            result += 1
            final_pos -= 100
        
        if final_pos == 0 or final_pos == 100:
            final_pos = 0
            result += 1
        curr_pos = final_pos
    print(f"Part 2: {result}")
    return result

if __name__ == "__main__":
    part1()
    part2()