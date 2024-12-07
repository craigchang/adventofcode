# https://adventofcode.com/2022/day/14

import matplotlib.pyplot as plt

# for visual purposes
def print_map(grid, sx = 500, sy = 0):
  xs = [pt[0] for pt in grid.keys() if grid[pt] == '#']
  ys = [-pt[1] for pt in grid.keys() if grid[pt] == '#']
  sand_xs = [pt[0] for pt in grid.keys() if grid[pt] == 'o']
  sand_ys = [-pt[1] for pt in grid.keys() if grid[pt] == 'o']

  plt.scatter(xs, ys)
  plt.scatter(sand_xs, sand_ys)
  plt.scatter(sx, -sy)
  plt.rcParams["figure.figsize"] = (15,15)
  plt.show()

def is_blocked(grid, x, y, curr_y, floor):
  return (x,y) in grid and (grid[(x,y)] == '#' or grid[(x,y)] == 'o') or curr_y == floor

def create_grid():
  with open("day14/input.txt", "r") as f:
    grid = dict()
    
    for l in f:
      rock_path = []
      tokens = l.strip().split(" -> ")
      for t in tokens:
        x, y = t.split(',')
        rock_path.append((int(x),int(y)))
      for i in range(0, len(rock_path)-1):
        (x1, y1), (x2, y2) = rock_path[i], rock_path[i+1]
        if x1 == x2:
          if y1 > y2:
            for j in range(y2, y1+1):
              grid[(x1,j)] = '#'
          else:
            for j in range(y1, y2+1):
              grid[(x1,j)] = '#'
        elif y1 == y2:
          if x1 > x2:
            for j in range(x2, x1+1):
              grid[(j,y1)] = '#'
          else:
            for j in range(x1, x2+1):
              grid[(j,y1)] = '#'
  return grid

def part1():
  grid = create_grid()
  max_y = 0
  for (x,y) in grid.keys():
    if max_y < y:
      max_y = y
  i = 0
  x, y = (500,0)
  while(True):
    if not is_blocked(grid,x,y+1,y,max_y+1):
      y += 1
    elif not is_blocked(grid,x-1,y+1,y,max_y+1):
      x, y = x-1, y+1
    elif not is_blocked(grid,x+1,y+1,y,max_y+1):
      x, y = x+1, y+1
    elif y > max_y: # passes lowest pt
      print(i)
      break
    else:
      grid[(x,y)] = 'o'
      x, y = (500,0)
      i += 1
  
  #print_map(grid) 
  return

def part2():
  grid = create_grid()
  max_y = 0
  for (x,y) in grid.keys():
    if max_y < y:
      max_y = y
  floor = max_y + 2
  i = 0
  x, y = (500,0)
  while(True):
    if not is_blocked(grid,x,y+1,y,floor-1):
      y += 1
    elif not is_blocked(grid,x-1,y+1,y,floor-1):
      x, y = x-1, y+1
    elif not is_blocked(grid,x+1,y+1,y,floor-1):
      x, y = x+1, y+1
    elif y == floor - 1: # if it hits the floor
      grid[(x,y)] = 'o'
      x, y = (500,0)
      i += 1
    elif x == 500 and y == 0: # all filled up
      i += 1
      print(i)
      break
    else:
      grid[(x,y)] = 'o'
      x, y = (500,0)
      i += 1
  
  #print_map(grid) 
  return

part1()
part2()
