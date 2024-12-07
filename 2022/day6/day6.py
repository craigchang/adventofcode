# https://adventofcode.com/2022/day/6

def findMarker(size_packet):
  with open("day6/input.txt", "r") as f:
    data = f.readline().strip()
    for i in range(len(data) - size_packet):
      for j in range(size_packet):
        if data[i:i+size_packet].count(data[i+j]) > 1: # find repeats
          break
      if j+1 == size_packet: # if no repeats found
        return i+size_packet

print("Part 1: ", findMarker(4))
print("Part 2: ", findMarker(14))