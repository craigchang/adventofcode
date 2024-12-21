# https://adventofcode.com/2024/day/13

import re

def find_prize(a_button, b_button, prize, max_presses = 0):
  (ax, ay), (bx, by), (px, py) = a_button, b_button, prize
  a_mult = (px * by - py * bx) / (ax * by - ay * bx)
  b_mult = (py- ay * a_mult) / by
  if a_mult != round(a_mult) or b_mult != round(b_mult): # only integers valid
    return 0
  elif not max_presses or (max_presses and a_mult + b_mult <= max_presses):
    return 3*int(a_mult) + int(b_mult)
  return 0

def read_file():
  cranes = list()
  with open("2024/day13/input.txt", "r") as f:
    for l in f.readlines():
      if not l.strip():
        continue
      elif l.strip().startswith("Button A"):
        a_button = tuple(map(int, re.search("Button A: X\+(\d+), Y\+(\d+)", l).groups()))
      elif l.strip().startswith("Button B"):
        b_button = tuple(map(int, re.search("Button B: X\+(\d+), Y\+(\d+)", l).groups()))
      elif l.strip().startswith("Prize: "):
        prize = tuple(map(int, re.search("Prize: X=(\d+), Y=(\d+)", l).groups()))
        cranes.append((a_button, b_button, prize))
  return cranes

def part1():
  cranes = read_file()
  total = 0
  for c in cranes:
    a_button, b_button, prize = c
    total += find_prize(a_button, b_button, prize, 200)
  print(total)

def part2():
  cranes = read_file()
  total = 0
  for c in cranes:
    a_button, b_button, prize = c
    prize = ((prize[0] + 10000000000000), (prize[1] + 10000000000000))
    total += find_prize(a_button, b_button, prize)
  print(total)

part1()
part2()
