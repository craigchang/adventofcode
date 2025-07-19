# https://adventofcode.com/2015/day/13

import re
from itertools import permutations

def parse_line(line):
    match = re.match(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).', line)
    person1, action, amount, person2 = match.groups()
    return person1, person2, int(amount) * (1 if action == 'gain' else -1)

def calculate_happiness(arrangement, preferences):
    happiness = 0
    n = len(arrangement)
    for i in range(n):
        person1, person2 = arrangement[i], arrangement[(i + 1) % n]
        happiness += preferences.get((person1, person2)) + preferences.get((person2, person1))
    return happiness

def calc_max_happiness(people, preferences):
    max_happiness = float('-inf')
    for arrangement in permutations(people):
        max_happiness = max(max_happiness, calculate_happiness(arrangement, preferences))
    return max_happiness

# part 1
people = set()
with open("2015/day13/input.txt") as f:
    preferences = dict()
    for l in f.readlines():
        person1, person2, amount = parse_line(l.strip())
        people.add(person1)
        preferences[(person1, person2)] = amount
print(calc_max_happiness(people, preferences))

# part 2
people.add("Myself")
for person in list(people):
    preferences[("Myself", person)] = 0
    preferences[(person, "Myself")] = 0
print(calc_max_happiness(people, preferences))