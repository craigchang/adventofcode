# https://adventofcode.com/2024/day/14

import re
import matplotlib.pyplot as plt

class Robot:
  def __init__(self, px, py, vx, vy):
    self.px = px
    self.py = py
    self.vx = vx
    self.vy = vy

def print_map(robots):
  xs = [r.px for r in robots]
  ys = [-r.py for r in robots]
  plt.scatter(xs, ys)
  plt.show()

def within_quadrant(x, y, min_x, max_x, min_y, max_y):
  return min_x <= x and x < max_x and min_y <= y and y < max_y

def count_second(robots, max_x, max_y):
  for r in robots:
    dx = r.px + r.vx
    dy = r.py + r.vy
    r.px = dx + max_x if dx < 0 else dx % max_x
    r.py = dy + max_y if dy < 0 else dy % max_y

def calc_safety_factor(robots, max_x, max_y):
  for i in range(100):
    count_second(robots, max_x, max_y)

  half_x = max_x // 2
  half_y = max_y // 2
  q1, q2, q3, q4 = 0, 0, 0, 0

  for r in robots:
    if within_quadrant(r.px, r.py, 0, half_x, 0, half_y):
      q1 += 1
    elif within_quadrant(r.px, r.py, half_x+1, max_x, 0, half_y):
      q2 += 1
    elif within_quadrant(r.px, r.py, 0, half_x, half_y+1, max_y):
      q3 += 1
    elif within_quadrant(r.px, r.py, half_x+1, max_x, half_y+1, max_y):
      q4 += 1
  return q1 * q2 * q3 * q4

def find_christmas_tree(robots, max_x, max_y):
  # based on input, pattern appears at 97s, then every 101s after that until tree appears
  for i in range(1, 1000000000000, 1):
    count_second(robots, max_x, max_y)
    if i == 7672:
      print_map(robots, max_x, max_y)
      break

def read_file():
  robots = list()
  with open("2024/day14/input.txt", "r") as f:
    for l in f.readlines():
      px,py,vx,vy = tuple(map(int, re.search("p=(\d+),(\d+) v=(-?\d+),(-?\d+)", l.strip()).groups()))
      robots.append(Robot(px,py,vx,vy))
  return robots

def part1():
  robots = read_file()
  max_x = max([r.px for r in robots]) + 1
  max_y = max([r.py for r in robots]) + 1
  print(calc_safety_factor(robots, max_x, max_y))

def part2():
  robots = read_file()
  max_x = max([r.px for r in robots]) + 1
  max_y = max([r.py for r in robots]) + 1
  find_christmas_tree(robots, max_x, max_y)
  
part1()
part2()