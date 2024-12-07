# https://adventofcode.com/2023/day/12

import re

def read_file(filepath):
  with open(filepath, "r") as f:
    lines = []
    for l in f.readlines():
      records, groups = l.strip().split()
      lines.append((list(records), [int(i) for i in groups.split(",")]))
    return lines

def is_valid(line, arr):
  ct = 0
  curr_arr = []
  for ch in line:
    if ch == "#":
      ct += 1
    else:
      if ct > 0:
        curr_arr.append(ct)
        ct = 0
  
  if ct > 0:
    curr_arr.append(ct)

  if len(curr_arr) != len(arr):
    return False
  else:
    for i in range(len(arr)):
      if curr_arr[i] != arr[i]:
        return False
    
  return True

def go_back(line: str, arr: list):
  if "?" not in line:
    if is_valid(line, arr):
      return 1
    else:
      return 0
  i = line.index("?")
  line[i] = "#"
  count1 = go_back(line, arr)
  line[i] = "."
  count2 = go_back(line, arr)
  line[i] = "?"

  return count1 + count2

def part1(filename: str):
  lines = read_file(filename)
  num_arr = 0
  for l, arr in lines:
    num_arr += go_back(l, arr)
    print(num_arr, l, arr)
  print(num_arr)


def part2(filename: str):
  lines = read_file(filename)
  num_arr = 0
  for l, arr in lines:
    l = l + ["?"] + l+ ["?"] + l+ ["?"] + l+ ["?"] + l
    arr = arr * 5
    num_arr += go_back(l, arr)
    print(num_arr, l, arr)
  print(num_arr)

part1("day12/sample.txt")
part2("day12/sample.txt")
