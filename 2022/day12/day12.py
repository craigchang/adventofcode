# https://adventofcode.com/2022/day/12

def get_elevation(e):
  if e == "S": return ord('a')
  elif e == "E": return ord('z')
  else: return ord(e)

def is_valid(grid, visited, x1, y1, x2, y2):
  return x2 >= 0 and x2 < len(grid[0]) and y2 >= 0 and y2 < len(grid) \
    and get_elevation(grid[y2][x2]) <= get_elevation(grid[y1][x1]) + 1 \
    and not visited[y2][x2]

def BFS(grid, src):
  x, y = src
  visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

  q = []
  q.append( (x, y, 0) )
  visited[y][x] = True

  while q:
    x,y,dist = q.pop(0)

    # finished
    if grid[y][x] == "E":
      return dist
    
    if is_valid(grid, visited, x, y, x+1, y): # right
      visited[y][x+1] = True
      q.append((x+1, y, dist+1))
    if is_valid(grid, visited, x, y, x, y+1): # down
      visited[y+1][x] = True
      q.append((x, y+1, dist+1))
    if is_valid(grid, visited, x, y, x-1, y): # left
      visited[y][x-1] = True
      q.append((x-1, y, dist+1))
    if is_valid(grid, visited, x, y, x, y-1): # up
      visited[y-1][x] = True
      q.append((x, y-1, dist+1))
  
  return -1

def part1():
  with open("day12/input.txt", "r") as f:
    grid = [list(line.strip()) for line in f]

  # find starting point
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == "S":
        grid[y][x] = "a" # starting point always 'a'
        src = (x,y)
  
  # perform BFS
  print(BFS(grid, src))

def part2():
  with open("day12/input.txt", "r") as f:
    grid = [list(line.strip()) for line in f]

  min_dist = float('inf')
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == "a" or grid[y][x] == "S":
        dist = BFS(grid, (x,y))
        if dist < min_dist and dist != -1:
          min_dist = dist
  
  print(min_dist)


part1()
part2()
