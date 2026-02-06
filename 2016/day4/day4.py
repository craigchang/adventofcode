# https://adventofcode.com/2016/day/4

import re
from collections import Counter

def read_lines(filename="input.txt"):
    with open(f"2016/day4/{filename}", "r") as f:
        return [line.strip() for line in f.readlines()]

def decryptLetter(letter, num):
    return chr((ord(letter) - 97 + num) % 26 + 97)

def part1():
    data = read_lines()
    result = 0
    for d in data:
        match = re.search(r"^(.+?)\[(.+?)\]$", d)
        rooms = "".join(match.groups()[0].split("-")[:-1])
        sector_id = int(match.groups()[0].split("-")[-1])
        checksum = match.groups()[1]
        char_counts = Counter(rooms)
        sorted_chars = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))
        top5 = "".join([char for char, _ in sorted_chars[:5]])
        if top5 == checksum:
            result += sector_id
    print(f"Part 1: {result}")

def part2():
    data = read_lines()
    result = 0
    for d in data:
        match = re.search(r"^(.+?)\[(.+?)\]$", d)
        rooms = match.groups()[0].split("-")[:-1]
        sector_id = int(match.groups()[0].split("-")[-1])
        message = ""
        for room in rooms:
            for r in room:
                message += decryptLetter(r, sector_id)
            message += " "
        if "northpole object storage" in message:
            result = sector_id
            break
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part1()
    part2()