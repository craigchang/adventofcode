# https://adventofcode.com/2015/day/3

def moveDir(m, x, y):
    if m == '<':    return x-1,y
    elif m == '>':  return x+1,y
    elif m == '^':  return x,y+1
    elif m == 'v':  return x,y-1

# part 1
with open("2015/day3/input.txt", "r") as f:
    moves = f.readline()
    visited, x, y = {(0,0)},0,0
    for m in moves:
        x,y = moveDir(m,x,y)
        visited.add((x,y))
    print(len(visited))

# part 2
with open("2015/day3/input.txt", "r") as f:
    moves = f.readline()
    visited, sX, sY, rX, rY = {(0,0)},0,0,0,0
    turn = 1
    for m in moves:
        if turn:
            sX, sY = moveDir(m,sX,sY)
            visited.add((sX,sY))
        else:
            rX, rY = moveDir(m,rX,rY)
            visited.add((rX,rY))
        turn = not turn
    print(len(visited))