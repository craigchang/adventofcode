# https://adventofcode.com/2015/day/3

def moveDir(move, x, y):
  if move == '^':
    y += 1
  elif move == 'v':
    y -= 1
  elif move == '>':
    x += 1
  elif move == '<':
    x -= 1
  return (x,y)

def part1():
  with open("2015/day3/input.txt", "r") as f:
    santa, x, y = {(0,0)}, 0, 0
    print(santa)
    for move in f.readline():
      x, y = moveDir(move, x, y)
      santa.add((x, y))
    print(santa)
    print(len(santa))

def part2():
  with open("2015/day3/input.txt", "r") as f:
    santa, x1, y1 = {(0,0)}, 0, 0
    robo, x2, y2 ={(0,0)}, 0, 0
    turn = 0 # 0 for santa, 1 for robo
    for move in f.readline():
      if (not turn):
        x1, y1 = moveDir(move, x1, y1)
        santa.add((x1, y1))
      else:
        x2, y2 = moveDir(move, x2, y2)
        robo.add((x2,y2))
      turn = not turn
    total = santa.union(robo)
    print(len(total))

part1()
part2()