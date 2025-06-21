# https://adventofcode.com/2015/day/2

# part 1
paper = 0
with open("2015/day2/input.txt") as f:
    for d in f.readlines():
        l, w, h = list(map(int, d.split('x')))
        paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
print(paper)

# part 2
paper = 0
with open("2015/day2/input.txt") as f:
    for d in f.readlines():
        l, w, h = list(map(int, d.split('x')))
        paper += sum(sorted([l,w,h])[0:2]) * 2 + (l*w*h)
print(paper)