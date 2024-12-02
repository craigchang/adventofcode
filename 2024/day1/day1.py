# https://adventofcode.com/2024/day/1

import re

def readLists():
  with open("2024/day1/input.txt", "r") as f:
    l1, l2 = list(), list()
    for line in f.readlines():
      n1, n2 = re.findall("(\d+)\s+(\d+)", line.strip())[0]
      l1.append(int(n1))
      l2.append(int(n2))
    l1.sort()
    l2.sort()
  return l1,l2

def part1():
  l1, l2 = readLists()
  print(sum([abs(x - y) for x, y in zip(l1,l2)]))

def part2():
  l1, l2 = readLists()
  mem, result = dict(), 0
  for i in l1:
    if i not in mem: # cache results
      mem[i] = l2.count(i)
    result += i * mem[i]
  print(result)

part1()
part2()