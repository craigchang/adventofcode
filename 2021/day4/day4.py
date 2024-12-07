# https://adventofcode.com/2021/day/4

def readFile():
    with open("./day4/input.txt", "r") as f:
        drawNumbers = list(map(int, f.readline().strip().split(",")))
        boards = []
        board = []
        f.readline() # empty line

        for line in f:
            if line.strip() == "":
                boards.append(board)
                board = []
            else:
                board.append(list(map(int, line.strip().split())))
                
        boards.append(board)
        return drawNumbers, boards


def isBingo(board):
    for row in range(5):
        if sum([1 for col in range(5) if board[row][col] == 'X']) == 5:
            return True
    for col in range(5):
        if sum([1 for row in range(5) if board[row][col] == 'X']) == 5:
            return True
    return False


def part1():
    drawNumbers, boards = readFile()
    winningBoard = []

    for num in drawNumbers:
        for board in boards:
            for row in range(5):
                for col in range(5):
                    if board[row][col] == num:
                        board[row][col] = 'X'
        
        for board in boards:
            if isBingo(board):
                winningBoard = board
                break
        
        if winningBoard:
            break

    unmarkedSum = sum([winningBoard[y][x] for y in range(5) for x in range(5) if winningBoard[y][x] != 'X'])
    print(unmarkedSum * num)


def part2():
    drawNumbers, boards = readFile()
    winningBoardIndices = []

    for num in drawNumbers:
        for board in boards:
            for row in range(5):
                for col in range(5):
                    if board[row][col] == num:
                        board[row][col] = 'X'
                        
        for i in range(len(boards)):
            if i not in winningBoardIndices and isBingo(boards[i]) :
                winningBoardIndices.append(i)
        
        if len(winningBoardIndices) == len(boards):
            break
    
    winningBoard = boards[winningBoardIndices[-1]]
    unmarkedSum = sum([winningBoard[y][x] for y in range(5) for x in range(5) if winningBoard[y][x] != 'X'])
    print(unmarkedSum * num)


part1()
part2()