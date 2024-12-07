# https://adventofcode.com/2022/day/4

import re
reg_exp = "(\d+)-(\d+),(\d+)-(\d+)"

def main():
  with open('day4/input.txt', 'r') as f:
    num_fully_contains = 0
    num_overlap = 0
    for line in f:
      id1_start, id1_end, id2_start, id2_end = re.search(reg_exp, line.strip()).groups()
      s1 = [str(i) for i in range(int(id1_start), int(id1_end) + 1)] # section 1
      s2 = [str(i) for i in range(int(id2_start), int(id2_end) + 1)] # section 2
      if set(s1) & set(s2) == set(s1) or set(s1) & set(s2) == set(s2):
        num_fully_contains += 1
      if set(s1) & set(s2) or set(s1) & set(s2):
        num_overlap += 1
  print("Part 1:", num_fully_contains)
  print("Part 2:", num_overlap)

main()