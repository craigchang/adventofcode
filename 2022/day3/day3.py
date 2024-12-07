# https://adventofcode.com/2022/day/3

alpha_dict = {l: i for i, l in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1)}

def part1():
  with open("day3/input.txt", "r") as f: 
    sum_priorities = 0
    for line in f:
      half_line_len = len(line.strip()) // 2
      sack = line[:half_line_len],line[half_line_len:]
      sum_priorities += alpha_dict[set(sack[0]).intersection(sack[1]).pop()]
  print(sum_priorities)

def part2():
  with open("day3/input.txt", "r") as f: 
    sacks = []
    sum_priorities = 0
    for line in f:
      sacks.append(line.strip())
      if len(sacks) == 3: # group of 3
        sum_priorities += alpha_dict[set(sacks[0]).intersection(sacks[1]).intersection(sacks[2]).pop()]
        sacks.clear()
  print(sum_priorities)

part1()
part2()