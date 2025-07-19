# https://adventofcode.com/2015/day/12

import re
import json

# part 1
total = 0
with open("2015/day12/input.txt") as f:
    l = f.readline().strip()
    for num in re.findall(r'(-?\d+)', l):
        total += int(num)
print(total)

# part 2
def sum_numbers(obj):
    if isinstance(obj, dict):
        if 'red' in obj.values():
            return 0
        return sum(sum_numbers(v) for v in obj.values())
    elif isinstance(obj, list):
        return sum(sum_numbers(item) for item in obj)
    elif isinstance(obj, int):
        return obj
    return 0

total = 0
with open("2015/day12/input.txt") as f:
    l = f.readline().strip()
    total = sum_numbers(json.loads(l))

print(total)