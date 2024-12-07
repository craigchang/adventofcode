# https://adventofcode.com/2021/day/3

def readFile():
    with open("./day3/input.txt", "r") as f:
        return [num.strip() for num in f]


def part1():
    binaryNums = readFile()
    numLength = len(binaryNums[0])
    listLength = len(binaryNums)
    gammaRate = ""

    for digit in range(numLength): 
        digitList = [binaryNums[num][digit] for num in range(listLength)] # check each digit for all binary numbers
        gammaRate += '1' if digitList.count('1') >= listLength / 2 else '0'

    gammaRate = int(gammaRate, 2)
    epsilonRate = 1 << numLength - 1 ^ gammaRate # ones complement

    print(gammaRate * epsilonRate)


def part2():
    binaryNums = readFile()
    numLength = len(binaryNums[0])

    binNums2 = binaryNums.copy()

    # check each digit for most occurances
    for digit in range(numLength):
        listLength = len(binNums2)
        digitList = [binNums2[num][digit] for num in range(listLength)]
        commonDigit = '1' if digitList.count('1') >= listLength / 2 else '0'
        binNums2 = [binNums2[y] for y in range(listLength) if binNums2[y][digit] == commonDigit]
        if len(binNums2) == 1: # if one number left, found
            break
    oxygenGeneratorRating = int(binNums2[0], 2)

    binNums2 = binaryNums.copy()

    # check each digit for least occurances
    for digit in range(numLength):
        listLength = len(binNums2)
        digitList = [binNums2[num][digit] for num in range(listLength)]
        uncommomDigit = '1' if digitList.count('1') < listLength / 2 else '0'
        binNums2 = [binNums2[y] for y in range(listLength) if binNums2[y][digit] == uncommomDigit]
        if len(binNums2) == 1:
            break
    CO2ScrubberRating = int(binNums2[0], 2)

    print(oxygenGeneratorRating * CO2ScrubberRating)


part1()
part2()