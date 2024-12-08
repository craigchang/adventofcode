# https://adventofcode.com/2024/day/8

from itertools import combinations

def is_coord_valid(x, y, max_x, max_y):
  return x >= 0 and x < max_x and y >= 0 and y < max_y

def find_antinodes_from_antenna(x, y, xd, yd, max_x, max_y, antinodes, multiple):
  multiplier = 1
  while is_coord_valid((x+xd*multiplier), (y+yd*multiplier), max_x, max_y):
    antinodes.add(((x+xd*multiplier),(y+yd*multiplier)))
    if not multiple:
      break
    multiplier += 1

def find_antinodes(pair_ant, max_x, max_y, antinodes, multiple=False):
  (x1,y1),(x2,y2) = pair_ant
  xd, yd = (x2-x1), (y2-y1)
  find_antinodes_from_antenna(x1, y1, -xd, -yd, max_x, max_y, antinodes, multiple)
  find_antinodes_from_antenna(x2, y2, xd, yd, max_x, max_y, antinodes, multiple)

def read_file():
  grid = list()
  freqs = dict()

  with open("2024/day8/input.txt", "r") as f:
    for l in f.readlines():
      grid.append(list(l.strip()))
  
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] != '.':
        if grid[y][x] not in freqs:
          freqs[grid[y][x]] = [(y,x)]
        else:
          freqs[grid[y][x]].append((y,x))

  return grid, freqs

def part1():
  grid, freqs = read_file()
  grid_height, grid_length = len(grid), len(grid[0])
  antinodes = set()

  for _,coords in freqs.items():
    for pair_ant in list(combinations(coords,2)):
      find_antinodes(pair_ant, grid_length, grid_height, antinodes)

  print(len(antinodes))

def part2():
  grid, freqs = read_file()
  grid_height, grid_length = len(grid), len(grid[0])
  antinodes = set()

  for _,coords in freqs.items():
    for pair_ant in list(combinations(coords,2)):
      antinodes.add(pair_ant[0])
      antinodes.add(pair_ant[1])
      find_antinodes(pair_ant, grid_length, grid_height, antinodes, True)

  print(len(antinodes))

part1()
part2()