# https://adventofcode.com/2024/day/12

def is_coord_valid(x, y, max_x, max_y):
  return x >= 0 and x < max_x and y >= 0 and y < max_y

def calc_num_sides(coords):
  sides = 0
  for coord in coords:
    x,y = coord
    if (x-1,y) not in coords and (x,y-1) not in coords:
      sides += 1
    if (x,y-1) not in coords and (x+1,y) not in coords:
      sides += 1
    if (x+1,y) not in coords and (x,y+1) not in coords:
      sides += 1
    if (x,y+1) not in coords and (x-1,y) not in coords:
      sides += 1
    if (x-1,y) in coords and (x,y-1) in coords and (x-1,y-1) not in coords:
      sides += 1
    if (x,y-1) in coords and (x+1,y) in coords and (x+1,y-1) not in coords:
      sides += 1
    if (x+1,y) in coords and (x,y+1) in coords and (x+1,y+1) not in coords:
      sides += 1
    if (x,y+1) in coords and (x-1,y) in coords and (x-1,y+1) not in coords:
      sides += 1
  return sides

def calc_perimeter(coords):
  perimeter = 0
  for (x,y) in coords:
    for xd,yd in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
      if (xd,yd) not in coords:
        perimeter += 1
  return perimeter

def find_region(grid,x,y,max_x,max_y,r,region: set):
  if grid[y][x] != r:
    return region
  else:
    for xd,yd in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
      if is_coord_valid(xd, yd, max_x, max_y) and grid[yd][xd] == r and (xd,yd) not in region:
        region.add((xd,yd))
        find_region(grid,xd,yd,max_x,max_y,r,region)
  return region

def find_regions(grid,max_x, max_y):
  regions = list()
  marked = set()
  for y in range(max_y):
    for x in range(max_x):
      if (x,y) not in marked:
        region = find_region(grid,x,y,max_x,max_y,grid[y][x],{(x,y)})
        regions.append(region)
        marked = marked.union(region)
  return regions

def read_file():
  grid = list()
  with open("2024/day12/input.txt", "r") as f:
    for l in f.readlines():
      grid.append(list(l.strip()))
  return grid

def main():
  grid = read_file()
  regions = find_regions(grid, len(grid[0]), len(grid))
  print(sum([calc_perimeter(r) * len(r) for r in regions]))
  print(sum([calc_num_sides(r) * len(r) for r in regions]))

main()