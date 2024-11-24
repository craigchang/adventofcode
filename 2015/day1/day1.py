# https://adventofcode.com/2015/day/1

def part1():
  with open("2015/day1/input.txt", "r") as f:
    print(sum([1 if f == '(' else -1 for f in f.readline()]))

def part2():
  with open("2015/day1/input.txt", "r") as f:
    curr, floors = 0, f.readline()
    for i, f in enumerate(floors):
      curr += 1 if f == '(' else -1
      if curr < 0:
        print(i+1)
        return

part1()
part2()