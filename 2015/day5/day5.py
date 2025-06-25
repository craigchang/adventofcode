# https://adventofcode.com/2015/day/5

import re

r1 = r"[aeiou]"                 # vowels
f2 = r"([a-z])\1"               # twice in row
r3 = r"^((?!ab|cd|pq|xy).)*$"   # does not contain

# day 1
with open("2015/day5/input.txt") as f:
    num_nice_str = 0
    for l in f.readlines():
        l = l.strip()
        if len(re.findall(r1, l)) >= 3 and re.findall(f2, l) and re.match(r3, l):
            num_nice_str += 1
    print(num_nice_str)

# day 2
r4 = r"([a-z]{2}).*\1"          # two letters w/o overlap
r5 = r"([a-z]).\1"              # one letter which repeats 

with open("2015/day5/input.txt") as f:
    num_nice_str = 0
    for l in f.readlines():
        l = l.strip()
        if re.findall(r4, l) and re.findall(r5, l):
            num_nice_str += 1
    print(num_nice_str)