# https://adventofcode.com/2024/day/9

def create_blocks(diskmap):
  blocks = list()
  id = 0
  for i, num in enumerate(diskmap):
    if i % 2 == 0:
      for j in range(int(num)):
        blocks.append(id)
      id += 1
    else:
      for j in range(int(num)):
        blocks.append('.')
  return blocks

def read_file():
  diskmap = ""
  with open("2024/day9/input.txt", "r") as f:
    diskmap = f.readline().strip()
  return diskmap

def calc_checksum(blocks):
  total = 0
  for i, block in enumerate(blocks):
    if block != '.':
      total += int(blocks[i]) * i
  return total

def part1():
  diskmap = read_file()
  blocks = create_blocks(diskmap)
  start = 0
  end = len(blocks) - 1

  while start < end:
    if blocks[start] != '.':
      start += 1
    else:
      if blocks[end] != '.':
        blocks[start] = blocks.pop()
        start += 1
        end -= 1
      else:
        blocks.pop()
        end -= 1
  
  print(calc_checksum(blocks))

def part2():
  diskmap = read_file()
  #diskmap = "2333133121414131402"
  blocks = create_blocks(diskmap)
  #print(blocks)
  start = 0
  end = len(blocks) - 1
  skip = set()

  file_group = list()
  while start < end:
    if blocks[start] != '.':
      start += 1
    else:
      start_group = start
      if blocks[end] != '.':
        while end > start_group:
          if blocks[end] == '.':
            end -= 1
            continue
          file_group = [blocks[end]]
          end -= 1
          while blocks[end] != '.' and file_group[0] == blocks[end]:
            file_group.insert(0, blocks[end])
            end -= 1

          while start_group <= end:
            if blocks[start_group] == '.':
              empty_block_ct = blocks[start_group:start_group+len(file_group)].count('.')
              if empty_block_ct >= len(file_group):
                for i in range(empty_block_ct):
                  blocks[start_group] = file_group[i]
                  blocks[end+i+1] = '.'
                  #skip.add(start_group)
                  start_group += 1
                break
              else:
                start_group += empty_block_ct
            else:
              start_group += 1
          
          if start_group >= end:
            break
      else:
        end -= 1
        
  #print(blocks)
  print(calc_checksum(blocks))
  return

part1()
part2()


# 6415163624282