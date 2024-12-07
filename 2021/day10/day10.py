# https://adventofcode.com/2021/day/10


def readFile():
    with open("./day10/input.txt", "r") as f:
        return [line.strip() for line in f]


def part1():
    scoreDict = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    lines = readFile()
    incomplete = []
    score = 0

    for line in lines:
        st = []
        corrupted = False
        for chunk in line:
            if len(st) == 0:
                st.append(chunk)
                continue
            if chunk == ')':
                if st[-1] == '(':
                    st.pop()
                else:
                    score += scoreDict[chunk]
                    corrupted = True
                    break
            elif chunk == ']':
                if st[-1] == '[':
                    st.pop()
                else:
                    score += scoreDict[chunk]
                    corrupted = True
                    break
            elif chunk == '}':
                if st[-1] == '{':
                    st.pop()
                else:
                    score += scoreDict[chunk]
                    corrupted = True
                    break
            elif chunk == '>':
                if st[-1] == '<':
                    st.pop()
                else:
                    score += scoreDict[chunk]
                    corrupted = True
                    break
            else:
                st.append(chunk)

        if not corrupted:
            incomplete.append(st)
    
    print(score)
    return incomplete


def part2(incompleteLines):
    scoreDict = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    scores = []

    for line in incompleteLines:
        score = 0
        while len(line) > 0:
            score = (score * 5) + scoreDict[line[-1]]
            line.pop()
        scores.append(score)

    scores.sort()
    print(scores[len(scores)//2])


part2(part1())