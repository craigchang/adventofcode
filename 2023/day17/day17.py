# https://adventofcode.com/2023/day/17

UP, LEFT, DOWN, RIGHT = 0,1,2,3

def read_file(filepath):
  with open(filepath, 'r') as f:
    return [l.strip() for l in f.readlines()]

def find_path(grid: list, max_x: int, max_y: int, dir: int, steps: int=0, heat: int=0, x: int=0, y: int=0):
  if (x,y) == (max_x-1, max_y-1): # destination
    return heat
  
  # move first
  if dir == RIGHT:
    x += 1
  elif dir == LEFT:
    x -= 1
  elif dir == UP:
    y -= 1
  elif dir == DOWN:
    y += 1

  if x < 0 or x >= max_x or y < 0 or y >= max_y: # out of bounds
    return float('inf')

  heat += int(grid[y][x])
  steps += 1

  if steps == 3:
    if dir == RIGHT or dir == LEFT:
      u = find_path(grid, max_x, max_y, UP, 0, heat, x, y)
      d = find_path(grid, max_x, max_y, DOWN, 0, heat, x, y)
      return min(u,d)
    elif dir == DOWN or dir == UP:
      r = find_path(grid, max_x, max_y, RIGHT, 0, heat, x, y)
      l = find_path(grid, max_x, max_y, LEFT, 0, heat, x, y)
      return min(r,l)
  else: # steps < 3
    if dir == RIGHT:
      r = find_path(grid, max_x, max_y, RIGHT, steps, heat, x, y)
      u = find_path(grid, max_x, max_y, UP, 0, heat, x, y)
      d = find_path(grid, max_x, max_y, DOWN, 0, heat, x, y)
      return min(r,u,d)
    elif dir == LEFT:
      l = find_path(grid, max_x, max_y, LEFT, steps, heat, x, y)
      u = find_path(grid, max_x, max_y, UP, 0, heat, x, y)
      d = find_path(grid, max_x, max_y, DOWN, 0, heat, x, y)
      return min(l,u,d)
    elif dir == DOWN: 
      d = find_path(grid, max_x, max_y, DOWN, steps, heat, x, y)
      r = find_path(grid, max_x, max_y, RIGHT, 0, heat, x, y)
      l = find_path(grid, max_x, max_y, LEFT, 0, heat, x, y)
      return min(d,r,l)
    elif dir == UP:
      u = find_path(grid, max_x, max_y, UP, steps, heat, x, y)
      r = find_path(grid, max_x, max_y, RIGHT, 0, heat, x, y)
      l = find_path(grid, max_x, max_y, LEFT, 0, heat, x, y)
      return min(u,r,l)
    
def main():
  grid = read_file("day17/sample.txt")
  max_x, max_y = len(grid[0]), len(grid)
  #visited = [[False for x in range(max_x)] for y in range(max_y)]
  r = find_path(grid, max_x, max_y, RIGHT)
  d = find_path(grid, max_x, max_y, DOWN)
  print(min(r,d))
main()