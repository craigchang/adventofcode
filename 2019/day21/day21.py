import intCodeProgram
import copy

def AND(X,Y):
    return True if X is True and Y is True else False

def OR(X,Y):
    return True if X is True or Y is True else False

def NOT(X,Y):
    return True if X is False else False

#def convertToAscii(inputScript):

def printOutput(output):
    out = "".join(map(str,output))
    print(out)


def main():
    intCode = intCodeProgram.readFile('day21/input.txt')

    output, ptr, relativeBase = intCodeProgram.execute(copy.deepcopy(intCode), [])
    output = list(map(chr, output))
    print(output)

    output, ptr, relativeBase = intCodeProgram.execute(copy.deepcopy(intCode), [78, 79, 84, 32, 65, 32, 74, 10, 87, 65, 76, 75, 10])
    output = list(map(chr, output))
    printOutput(output)




main()
