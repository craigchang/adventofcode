# https://adventofcode.com/2021/day/14

def readFile():
    with open("./day14/input.txt", "r") as f:
        template = list(f.readline().strip())
        f.readline() # empty line
        pairs = {}
        for line in f:
            a, b = line.strip().split(' -> ')
            pairs[a] = b
        return template, pairs


def part1():
    template, pairs = readFile()
    for step in range(10):
        newTemplate = template.copy()
        j = 0
        for i in range(len(template) - 1):
            pr = "".join(template[i:i+2])
            j += 1 # position insert index between pair
            if pr in pairs:
                newTemplate.insert(j, pairs[pr])
                j += 1 # readjust insert index
        template = newTemplate.copy()
    counts = [template.count(c) for c in list(set(template))]
    print(max(counts) - min(counts))


def part2():
    template, pairs = readFile()
    pairsDict = {}

    # init pairsDict
    for i in range(len(template)-1):
        pr = "".join(template[i:i+2])
        pairsDict[pr] = 1 if pr not in pairsDict else pairsDict[pr] + 1
    
    for step in range(40):
        temp = {}
        for pr, ct in pairsDict.items():
            ins = pairs[pr]
            pr1, pr2 = pr[0] + ins, ins + pr[1]
            temp[pr1] = ct if pr1 not in temp else temp[pr1] + ct
            temp[pr2] = ct if pr2 not in temp else temp[pr2] + ct
                
        pairsDict = dict(sorted(temp.copy().items()))
    
    results = {}
    for pr, ct in pairsDict.items():
        pr1, pr2 = pr[0], pr[1]
        results[pr1] = ct/2 if pr1 not in results else results[pr1] + ct/2
        results[pr2] = ct/2 if pr2 not in results else results[pr2] + ct/2

    print(int(max(results.values()) - min(results.values()))) # actual answer differs by 1

part1()
part2()
