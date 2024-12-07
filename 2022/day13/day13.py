# https://adventofcode.com/2022/day/13

import ast 
from itertools import zip_longest
from functools import cmp_to_key

def is_right_order(p1, p2):
  for v1, v2 in zip_longest(p1, p2):
    if v1 == None and v2 != None:
      return -1
    elif v1 != None and v2 == None:
      return 1
    elif type(v1) == int and type(v2) == int:
      if v1 < v2:
        return -1
      elif v1 > v2:
        return 1
    else: # at least 1 list
      c1 = [v1] if type(v1) == int else v1
      c2 = [v2] if type(v2) == int else v2
      res = is_right_order(c1, c2)
      if res:
        return res
  return 0

def main(file_name):
  with open(file_name, "r") as f:
    packets = [ast.literal_eval(l.strip()) for l in f if l.strip()]

  # part 1
  sum_pairs = 0
  num_pair = 1

  for i in range(0, len(packets), 2):
    if is_right_order(packets[i], packets[i+1]) < 0:
      sum_pairs += num_pair
    num_pair += 1
  print(sum_pairs)

  # part 2
  packets.append([[2]])
  packets.append([[6]])
  
  sorted_packets = sorted(packets, key=cmp_to_key(is_right_order))

  num_packet = 1
  decoder_key = 1
  
  for packet in sorted_packets:
    if packet == [[2]] or packet == [[6]]:
      decoder_key *= num_packet
    num_packet += 1
  
  print(decoder_key)

main("day13/sample.txt")
main("day13/input.txt")
