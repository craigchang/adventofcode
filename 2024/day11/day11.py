# https://adventofcode.com/2024/day/11

def get_new_stones(stone):
  stone_str = str(stone)
  new_stone = list()
  if stone == 0:
    new_stone.append(1)
  elif len(stone_str) % 2 == 0:
    half1 = int(stone_str[:len(stone_str)//2])
    half2 = int(stone_str[len(stone_str)//2:])
    new_stone.extend([half1,half2])
  else:
    new_stone.append(stone * 2024)
  return new_stone

def calc_num_stones(blinks, stone_counter):
  for blink in range(blinks):
    stone_dict_new = dict()
    for stone, ct in stone_counter.items():
      for new_stone in get_new_stones(stone):
        if new_stone in stone_dict_new:
          stone_dict_new[new_stone] += ct
        else:
          stone_dict_new[new_stone] = ct
    stone_counter = stone_dict_new.copy()
  return sum(stone_counter.values())

def read_file():
  stones = list()
  with open("2024/day11/input.txt", "r") as f:
    stones = list(map(int, f.readline().strip().split(" ")))

  stone_counter = dict()
  for stone in stones:
    if stone in stone_counter:
      stone_counter[stone] += 1
    else:
      stone_counter[stone] = 1
  return stone_counter

def main():
  print(calc_num_stones(25, read_file()))
  print(calc_num_stones(75, read_file()))
  
main()