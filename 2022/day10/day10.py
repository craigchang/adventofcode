# https://adventofcode.com/2022/day/10

import re

def calc_signal_strengths(reg_x_cycles: dict):
  total = 0
  reg_x = 1
  cycles_list = [20, 60, 100, 140, 180, 220]
  for c in range(1, max(reg_x_cycles.keys()) + 1):
    if c in reg_x_cycles:
      reg_x += reg_x_cycles[c]
    if c in cycles_list:
      total += c * reg_x
  return total

def render_image(reg_x_cycles: dict):
  reg_x = 0
  sprite_pos = [0,1,2]
  crt = [[''] * 40 for i in range(6)]
  for c in range(1, max(reg_x_cycles.keys()) + 1):
    if c in reg_x_cycles:
      reg_x += reg_x_cycles[c]     
      sprite_pos = [reg_x, reg_x+1, reg_x+2]
    col, row = (c-1)//40, (c-1) % 40
    crt[col][row] = '#' if row in sprite_pos else '.'
  for col in crt:
    print("".join(col))

def main():
  with open("day10/input.txt", "r") as f:
    clock = 1
    reg_x_cycles = {}

    for line in f:
      instr = line.strip()
      if instr.startswith("addx"):
        clock += 2
        reg_x_cycles[clock] = int(instr.split()[1])
      else:
        clock += 1

    print(calc_signal_strengths(reg_x_cycles)) # part 1
    render_image(reg_x_cycles) # part 2

main()