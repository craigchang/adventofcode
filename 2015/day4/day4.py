# https://adventofcode.com/2015/day/4

import hashlib

def calcHash(input, numZeroes):
  i, zeroes = 0, numZeroes*'0'
  while True:
    if hashlib.md5((input + str(i)).encode()).hexdigest()[:numZeroes] == zeroes:
      return i
    i += 1

print(calcHash("yzbqklnj", 5)) # part 1
print(calcHash("yzbqklnj", 6)) # part 2