# https://adventofcode.com/2015/day/1

# part 1
with open("2015/day1/input.txt", "r") as f:
    print(sum([1 if s == "(" else -1 for s in f.readline()]))

# part 2
with open("2015/day1/input.txt", "r") as f:
    curr = 0
    for i, s in enumerate(f.readline()):
        curr += 1 if s == "(" else -1
        if curr < 0:
            print(i+1)
            break