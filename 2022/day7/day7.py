# https://adventofcode.com/2022/day/7

import re
from helper import get_nested_value, set_nested_value

def calc_dir_size(fs: dict, ignore=""):
  size = 0
  for k in fs.keys():
    if ignore == k:
      continue
    size += calc_dir_size(fs[k]) if type(fs[k]) == dict else fs[k]
  return size

def parse_file():
  with open("day7/input.txt", "r") as f:
    fs = {}
    directories = {}
    path = []
    lines = [l.strip() for l in f.readlines()]

    for l in lines:
      if l.startswith("$ cd"):
        d, = re.search("\$ cd (.+)", l).groups()
        if d == "..": # prev dir
          path.pop()
        else:
          path.append(d)
          directories[tuple(path)] = d
      elif l.startswith("$ ls"): # not really used
        continue
      elif l.startswith("dir"): # if directory
        sub_dir, = re.search("dir (.+)", l).groups()
        set_nested_value(fs, path + [sub_dir], {}, True)
      else: # is a file
        file_size, file = re.search("(.+) (.+)", l).groups()
        set_nested_value(fs, path + [file], int(file_size), True)
  return fs, directories

def part1():
  fs, directories = parse_file()
  sum_sizes = 0
  for path in directories.keys():
    sum_size = calc_dir_size(get_nested_value(fs, path))
    sum_sizes += sum_size if sum_size <= 100000 else 0
  print(sum_sizes)

def part2():
  fs, directories = parse_file()
  deleted_mem = 0
  unused_space = 70000000 - calc_dir_size(get_nested_value(fs, ("/")))
  min_space_needed = float('inf')
  
  for path, dir in directories.items():
    deleted_space = calc_dir_size(get_nested_value(fs, path[:-1])) - calc_dir_size(get_nested_value(fs, path[:-1]), path[-1])
    min_unused_space = unused_space + deleted_space
    if min_unused_space > 30000000 and min_space_needed > min_unused_space:
      min_space_needed = min_unused_space
      deleted_mem = deleted_space
  print(deleted_mem)

part1()
part2()