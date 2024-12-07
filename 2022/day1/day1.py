# https://adventofcode.com/2022/day/1

def readFile():
  with open("day1/input.txt", "r") as f:
    elves, calories = [], 0
    for l in (f.readlines() + ['']): # padding end of file
      if l.strip():
        calories += int(l.strip())
      else:
        elves.append(calories)
        calories = 0
    return elves

def part1():
  elves = readFile()
  elves.sort(reverse=True)
  print(elves[0]) # top 1

def part2():
  elves = readFile()
  elves.sort(reverse=True)
  print(sum(elves[:3])) # top 3

part1()
part2()