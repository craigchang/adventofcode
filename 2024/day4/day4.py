# https://adventofcode.com/2024/day/4

possibleMAS = (((-1,-1),(1,1),(1,-1),(-1,1)),
    ((-1,-1),(1,1),(-1,1),(1,-1)),
    ((1,-1),(-1,1),(1,1),(-1,-1)),
    ((1,1),(-1,-1),(-1,1),(1,-1)))

def findXMAS(grid, x, y, dx, dy):
  if grid[y][x] != 'X' or (y+dy*3) < 0 or (y+dy*3) >= len(grid) or (x+dx*3) < 0 or (x+dx*3) >= len(grid[0]):
    return False
  if grid[y+dy][x+dx] == 'M' and grid[y+dy*2][x+dx*2] == 'A' and grid[y+dy*3][x+dx*3] == 'S':
    return True
  return False

def findMAS(grid, x, y):
  if grid[y][x] != 'A' or y-1 < 0 or x-1 < 0 or y+1 >= len(grid) or x+1 >= len(grid[0]):
    return False
  for (m1y, m1x), (s1y, s1x), (m2y, m2x), (s2y, s2x) in possibleMAS:
    if grid[y+m1y][x+m1x] == 'M' and grid[y+s1y][x+s1x] == 'S' and \
      grid[y+m2y][x+m2x] == 'M' and grid[y+s2y][x+s2x] == 'S':
      return True
  return False

def readFile():
  with open("2024/day4/input.txt", "r") as f:
    return [list(line.strip()) for line in f.readlines()]

def part1():
  grid = readFile()
  count = 0
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == 'X':
        for dy, dx in ((-1,-1),(-1,0),(0,-1),(1,1),(1,0),(0,1),(-1,1),(1,-1)):
          if findXMAS(grid, x, y, dx, dy):
            count += 1
  print(count)

def part2():
  grid = readFile()
  count = 0
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == 'A' and findMAS(grid, x, y):
        count += 1
  print(count)

part1()
part2()