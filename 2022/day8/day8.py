# https://adventofcode.com/2022/day/8

def is_tree_visible(trees, x, y, max_row, max_col):
  for left in range(x-1, -1, -1):
    if trees[y][left] >= trees[y][x]:
      break
  else:
    return True
  
  for right in range(x+1, max_row, 1):
    if trees[y][right] >= trees[y][x]:
      break
  else:
    return True

  for top in range(y-1, -1, -1):
    if trees[top][x] >= trees[y][x]:
      break
  else:
    return True

  for bottom in range(y+1, max_col, 1):
    if trees[bottom][x] >= trees[y][x]:
      break
  else:
    return True

  return False

def calc_scenic_score(trees, x, y, max_row, max_col):
  scenic_score = 1

  num_trees = 0
  for left in range(x-1, -1, -1):
    num_trees += 1
    if trees[y][left] >= trees[y][x]:
      break
  scenic_score *= num_trees

  num_trees = 0
  for right in range(x+1, max_row, 1):
    num_trees += 1
    if trees[y][right] >= trees[y][x]:
      break
  scenic_score *= num_trees
  
  num_trees = 0
  for top in range(y-1, -1, -1):
    num_trees += 1
    if trees[top][x] >= trees[y][x]:
      break
  scenic_score *= num_trees
  
  num_trees = 0
  for bottom in range(y+1, max_col, 1):
    num_trees += 1
    if trees[bottom][x] >= trees[y][x]:
      break
  scenic_score *= num_trees

  return scenic_score

def part1():
  with open("day8/input.txt", "r") as f:
    trees = [[int(t) for t in line.strip()] for line in f]
    max_row, max_col, num_visible = len(trees[0]), len(trees), 0
    num_visible = 0
    for y in range(max_col):
      for x in range(max_row):
        if x == 0 or y == 0 or x == max_row-1 or y == max_col-1: # edges are visible
          num_visible += 1
        elif is_tree_visible(trees, x, y, max_row, max_col):
          num_visible += 1
  print(num_visible)
          
def part2():
  with open("day8/input.txt", "r") as f:
    trees = [[int(t) for t in line.strip()] for line in f]
    max_row, max_col = len(trees[0]), len(trees)
    max_scenic_score = 0
    for y in range(max_col):
      for x in range(max_row):
        if x == 0 or y == 0 or x == max_row-1 or y == max_col-1: # edges are 0
          continue
        else:
          scenic_score = calc_scenic_score(trees, x, y, max_row, max_col)
          if max_scenic_score < scenic_score:
            max_scenic_score = scenic_score
    print(max_scenic_score)

part1()
part2()
