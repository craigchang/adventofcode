# https://adventofcode.com/2021/day/6

def readFile():
    with open("./day6/sample.txt", "r") as f:
        return list(map(int, f.readline().strip().split(",")))

def part1():
    fishes = readFile()
    
    for day in range(50):
        currentLength = len(fishes)
        #print('day: ', day+1, currentLength)
        for i in range(currentLength):
            if fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] -= 1
        print(fishes)

    print(fishes)
    print(len(fishes))

    # expoRate = dict()
    
    # for i in range(1,7):
    #     curr = [i]
    #     for day in range(30):
    #         #print(day)
    #         currentLength = len(curr)
    #         for j in range(currentLength):
    #             if curr[j] == 0:
    #                 curr[j] = 6
    #                 curr.append(8)
    #             else:
    #                 curr[j] -= 1

    #     if i not in expoRate:
    #         expoRate[i] = len(curr)
    #     print(i, len(curr))

    # print(sum([expoRate[fish] for fish in fishes]))




def part2():
    fishes = readFile()
    
    for day in range(256):
        currentLength = len(fishes)
        print(day, len(fishes))
        for i in range(currentLength):
            if fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] -= 1

    print(len(fishes))

part1()
part2()