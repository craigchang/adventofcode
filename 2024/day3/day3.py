# https://adventofcode.com/2024/day/3

import re

def part1():
  with open("2024/day3/input.txt", "r") as f:
    results = 0
    for line in f.readlines():
      muls = re.findall("mul\((\d+),(\d+)\)", line.strip())
      for mul in muls:
        results += int(mul[0]) * int(mul[1])
    print(results)

def part2():
  with open("2024/day3/input.txt", "r") as f:
    results, enabled = 0, True
    for line in f.readlines():
      muls = re.findall("mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line.strip())
      for mul in muls:
        num1, num2, do, dont = mul
        if do:
          enabled = True
        elif dont:
          enabled = False
        elif enabled:
          results += int(num1) * int(num2)
    print(results)

part1()
part2()