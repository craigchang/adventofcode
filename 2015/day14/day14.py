# https://adventofcode.com/2015/day/14

import re

def parse_reindeer(line):
    match = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
    reindeer = match.group(1)
    speed = int(match.group(2))
    fly_time = int(match.group(3))
    rest_time = int(match.group(4))
    return reindeer, speed, fly_time, rest_time

def calculate_distance(speed, fly_time, rest_time, total_time):
    total_cycle_time = fly_time + rest_time
    full_cycles = total_time // total_cycle_time
    remaining_time = total_time % total_cycle_time
    distance = full_cycles * speed * fly_time
    if remaining_time > fly_time and remaining_time <= total_cycle_time:
        distance += speed * fly_time
    elif remaining_time <= fly_time:
        distance += speed * remaining_time
    return distance

# part 1
with open("2015/day14/input.txt") as f:
    max_distance = 0
    for line in f.readlines():
        reindeer, speed, fly_time, rest_time = parse_reindeer(line.strip())
        max_distance = max(max_distance, calculate_distance(speed, fly_time, rest_time, 2503))
    print(max_distance)

# part 2
with open("2015/day14/input.txt") as f:
    reindeer_list = list()
    distances = {}
    points = {}
    for line in f.readlines():
        reindeer, speed, fly_time, rest_time = parse_reindeer(line.strip())
        reindeer_list.append((reindeer, speed, fly_time, rest_time))
        distances[reindeer] = 0
        points[reindeer] = 0

    for second in range(1, 2504):
        for reindeer, speed, fly_time, rest_time in reindeer_list:
            distances[reindeer] = calculate_distance(speed, fly_time, rest_time, second)
        max_distance = max(distances.values())
        for reindeer, distance in distances.items():
            if distance == max_distance:
                points[reindeer] += 1
    print(max(points.values()))