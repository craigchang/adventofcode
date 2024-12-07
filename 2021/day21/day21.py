# https://adventofcode.com/2021/day/21


def readFile():
    with open("./day21/sample.txt", "r") as f:
        p1_start = f.readline().strip().split(": ")[1]
        p2_start = f.readline().strip().split(": ")[1]
        return int(p1_start), int(p2_start)


def part1():
    p1_space, p2_space = readFile()
    p1_turn = True
    p1_score, p2_score = 0,0
    die_val = 1
    rolls = 0
    max_score = 1000
    die_size = 100

    while(True):
        dice = 0 # reset die
        for x in range(3):
            dice += die_val
            die_val += 1
            if die_val > die_size:
                die_val %= die_size
        if p1_turn:
            p1_space += dice
            p1_score += 10 if p1_space % 10 == 0 else p1_space % 10
        else:
            p2_space += dice
            p2_score += 10 if p2_space % 10 == 0 else p2_space % 10
        p1_turn = not p1_turn
        rolls += 1

        if p1_score >= max_score:
            print(rolls * 3 * p2_score)
            break
        if p2_score >= max_score:
            print(rolls * 3 * p1_score)
            break


def part2():
    return       


part1()
part2()