# https://adventofcode.com/2015/day/2

import re

def part1():
  with open("2015/day2/input.txt", "r") as f:
    area = 0
    for box in f.readlines():
      l,w,h = [int(i) for i in box.split("x")]
      area += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    print(area)

def part2():
  with open("2015/day2/input.txt", "r") as f:
    area = 0
    for box in f.readlines():
      l1,l2,l3 = sorted([int(i) for i in box.split("x")])
      area += 2*l1 + 2*l2 + l1*l2*l3
    print(area)
    
part1()
part2()