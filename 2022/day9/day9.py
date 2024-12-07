# https://adventofcode.com/2022/day/9

import re

def move_head(dir, steps, rope, positions):
  # loop n steps
  for i in range(steps):
    # move head
    if dir == 'R': rope[0][0] += 1
    elif dir == "L": rope[0][0] -= 1
    elif dir == "U": rope[0][0] += 1
    else: rope[0][0] -= 1

    # loop through all knots
    for i in range(len(rope)-1):
      next1_x, next1_y = rope[i]
      next2_x, next2_y = rope[i+1]

      # move tail
      if next1_x - next2_x > 1:
        next2_x += 1
        if next1_y - next2_y >= 1:
          next2_y += 1
        elif next2_y - next1_y >= 1:
          next2_y -= 1
      elif next2_x - next1_x > 1:
        next2_x -= 1
        if next1_y - next2_y >= 1:
          next2_y += 1
        elif next2_y - next1_y >= 1:
          next2_y -= 1
      elif next1_y - next2_y > 1:
        next2_y += 1
        if next1_x - next2_x >= 1:
          next2_x += 1
        elif next2_x - next1_x >= 1:
          next2_x -= 1
      elif next2_y - next1_y > 1:
        next2_y -= 1
        if next1_x - next2_x >= 1:
          next2_x += 1
        elif next2_x - next1_x >= 1:
          next2_x -= 1
      
      rope[i+1] = [next2_x, next2_y]
    
    positions.add(tuple(rope[-1])) # record tail pos

def main(rope):
  positions = set()
  positions.add((0,0))
  with open("day9/input.txt", "r") as f:
    for line in f:
      dir, steps = re.search("(.+) (\d+)", line.strip()).groups()
      move_head(dir, int(steps), rope, positions)
  print(len(positions))

main([[0,0]] * 2)   # part1
main([[0,0]] * 10)  # part2
