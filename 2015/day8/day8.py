# https://adventofcode.com/2015/day/8

import re

# part 1
num_orig = 0
num_new = 0
with open("2015/day8/input.txt") as f:
    for l in f.readlines():
        l = l.strip()
        num_orig += len(l)
        s = re.findall(r'"(.*)"', l)[0]
        num_new += len(s.encode('utf-8').decode('unicode_escape'))
print(num_orig - num_new)

# part 2
num_orig = 0
num_new = 0
with open("2015/day8/input.txt") as f:
    for l in f.readlines():
        l = l.strip()
        num_orig += len(l)
        s = l.replace("\\", "\\\\").replace('"', '\\"')
        num_new += len('"' + s + '"')
print(num_new - num_orig)
