# https://adventofcode.com/2024/day/6

UP, RIGHT, DOWN, LEFT = 0,1,2,3

def rotate_90(dir):
  return dir+1 if dir < 3 else 0

def find_guard_positions(grid, guard, dir):
  grid_size = len(grid) * len(grid[0])
  distinct = set()
  distinct.add(guard)
  y, x = guard
  num_steps = 0

  while y > 0 and x > 0 and num_steps < grid_size:
    if dir == UP:
      if y-1 < 0:
        break
      elif grid[y-1][x] == '#':
        dir = rotate_90(dir)
      else:
        y -= 1
    elif dir == RIGHT:
      if x+1 >= len(grid[0]):
        break
      elif grid[y][x+1] == '#':
        dir = rotate_90(dir)
      else:
        x += 1
    elif dir == DOWN:
      if y+1 >= len(grid):
        break
      elif grid[y+1][x] == '#':
        dir = rotate_90(dir)
      else:
        y += 1
    elif dir == LEFT:
      if x-1 < 0:
        break
      elif grid[y][x-1] == '#':
        dir = rotate_90(dir)
      else:
        x -= 1
    num_steps += 1
    distinct.add((y,x))
    
  if num_steps >= grid_size:
    return -1, distinct
  else:
    return len(distinct), distinct

def find_guard(grid):
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == '^':
        return (y,x)

def readFile():
  grid = []
  with open("2024/day6/input.txt", "r") as f:
    for line in f.readlines():
      grid.append(list(line.strip()))
  return grid

def part1():
  grid = readFile()
  guard = find_guard(grid)
  result, _ = find_guard_positions(grid, guard, UP)
  print(result)

def part2():
  grid = readFile()
  guard = find_guard(grid)
  _, orig_distinct = find_guard_positions(grid, guard, UP)
  num_pos = 0

  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == '#' or grid[y][x] == '^' or (y,x) not in orig_distinct:
        continue
      new_grid = [r[:] for r in grid]
      new_grid[y][x] = '#'
      result, _ = find_guard_positions(new_grid, guard, UP)
      if result == -1:
        num_pos += 1

  print(num_pos)

part1()
part2()