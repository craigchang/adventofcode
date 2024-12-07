# https://adventofcode.com/2022/day/5

import re
regexp = "move (\d+) from (\d+) to (\d+)"

def parseStacks(f):
  lines = []
  for l in f:
    if l == "\n":
      break
    lines.append([l[i:i+3] for i in range(0, len(l), 4)])
  lines.reverse()

  st = []
  stacks = []
  for c in range(len(lines[0])):
    for r in range(1, len(lines)):
      if lines[r][c].strip() != '':
        st.append(lines[r][c])
    stacks.append(st)
    st = []
  return stacks

def moveCrates(f, stacks: list, multiple=False):
  for l in f:
    num_crates, source, target = re.search(regexp, l.strip()).groups()
    num_crates, source, target = int(num_crates), int(source)-1, int(target)-1
    if not multiple: # move crate 1 by 1
      stacks[target] += [stacks[source].pop() for i in range(num_crates)]
    else: # move crates together
      stacks[target] += stacks[source][-num_crates:]
      [stacks[source].pop() for i in range(num_crates)]

def part1():
  with open("day5/input.txt", "r") as f:
    stacks = parseStacks(f)
    moveCrates(f, stacks)
    print([crate[-1] for crate in stacks])

def part2():
  with open("day5/input.txt", "r") as f:
    stacks = parseStacks(f)
    moveCrates(f, stacks, True)
    print([crate[-1] for crate in stacks])

part1()
part2()