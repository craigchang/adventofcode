# https://adventofcode.com/2024/day/10

def is_coord_valid(x, y, max_x, max_y):
  return x >= 0 and x < max_x and y >= 0 and y < max_y

def find_trails(grid: list, x, y, max_x, max_y, peaks: set, trails: list):
  if grid[y][x] == 9:
    trails.append(1)
    peaks.add((x,y))
  else:
    for xd, yd in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
      if is_coord_valid(xd, yd, max_x, max_y) and grid[yd][xd] == grid[y][x] + 1:
        find_trails(grid, xd, yd, max_x, max_y, peaks, trails)

def calc_scores_ratings(grid):
  scores, ratings = 0, 0
  max_x, max_y = len(grid[0]), len(grid)
  for y in range(max_y):
    for x in range(max_x):
      if grid[y][x] == 0:
        peaks, trails = set(), list()
        find_trails(grid, x, y, max_x, max_y, peaks, trails)
        scores += len(peaks)
        ratings += len(trails)
  return scores, ratings

def read_file():
  grid = list()
  with open("2024/day10/input.txt", "r") as f:
    for l in f.readlines():
      grid.append(list(map(int, l.strip())))
  return grid

def main():
  scores, ratings = calc_scores_ratings(read_file())
  print(scores)
  print(ratings)

main()
