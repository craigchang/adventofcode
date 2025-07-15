# https://adventofcode.com/2015/day/9

import re

# part 1
locations = set()
distances = dict()
with open("2015/day9/input.txt") as f:
    for l in f.readlines():
        depart, dest, dist = re.findall(r'(\w+) to (\w+) = (\d+)', l.strip())[0]
        locations.add(depart)
        locations.add(dest)
        dist = int(dist)
        distances[(depart, dest)] = dist
        distances[(dest, depart)] = dist

queue = [(0, list(locations), [])]
min_dist = float('inf')
while queue:
    curr_dist, remaining_locations, path = queue.pop(0)
    if not remaining_locations:
        min_dist = min(min_dist, curr_dist)
        continue
    
    for loc in remaining_locations:
        new_remaining = remaining_locations[:]
        new_remaining.remove(loc)
        new_distance = curr_dist
        if path:
            new_distance += distances.get((path[-1], loc), distances.get((loc, path[-1]), 0))
        queue.append((new_distance, new_remaining, path + [loc]))

print(min_dist)

# part 2
max_dist = 0
queue = [(0, list(locations), [])]
while queue:
    curr_dist, remaining_locations, path = queue.pop(0)
    if not remaining_locations:
        max_dist = max(max_dist, curr_dist)
        continue
    
    for loc in remaining_locations:
        new_remaining = remaining_locations[:]
        new_remaining.remove(loc)
        new_distance = curr_dist
        if path:
            new_distance += distances.get((path[-1], loc), distances.get((loc, path[-1]), 0))
        queue.append((new_distance, new_remaining, path + [loc]))

print(max_dist)

