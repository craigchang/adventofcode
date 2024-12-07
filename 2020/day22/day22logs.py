def readFile():
    with open("day22/input.txt", "r") as file:
        p1 = []
        p2 = []
        for line in file:
            if line.startswith("\n"):
                break
            elif not line.startswith("Player 1:"):
                p1.append(int(line))
        for line in file:
            if line.startswith("\n"):
                break
            elif not line.startswith("Player 2:"):
                p2.append(int(line))
        return p1, p2

def playGame(p1, p2):
    turn = 0

    while(len(p1) != 0 and len(p2) != 0):
        turn += 1
        print("-- Round", turn, "--")
        print("Player 1's deck:", p1)
        print("Player 2's deck:", p2)

        v1 = p1.pop(0)
        v2 = p2.pop(0)

        print("Player 1 plays:", v1)
        print("Player 2 plays:", v2)

        if (v1 > v2):
            print("Player 1 wins the round!")
            p1.append(v1)
            p1.append(v2)
        else:
            print("Player 2 wins the round!")
            p2.append(v2)
            p2.append(v1)
        print()

    return p1 if len(p1) > 0 else p2

def part1():
    p1, p2 = readFile()
    pwon = playGame(p1, p2)

    score = 0
    if len(pwon) > 0:
        pwon = pwon[::-1]
        for i in range(1, len(pwon) + 1):
            score += (i * pwon[i-1])
    print(score)

def determineRoundWinner(p1, p2, history):
    if p1 in history[1] and p2 in history[2]:
        print("Player 1 wins the round! (duplicate round!)")
        return True
    return False



def playGame2(p1, p2, game=1, subGame=[1]):
    turn = 0
    historyList = []

    print()
    print(f"=== Game {game} ===")
    
    while(len(p1) != 0 and len(p2) != 0):
        turn += 1
        print(f"-- Round {turn} of (Game {game}) --")
        print(f"Player 1's deck:", ",".join([str(n) for n in p1]))
        print(f"Player 2's deck:", ",".join([str(n) for n in p2]))

        #if p1 in history[1] and p2 in history[2] and history[1].index(p1) == history[2].index(p2):
        if ([p1,p2] in historyList):
            print("Player 1 wins the game! (duplicate round!)")
            return p1, "1"

        historyList.append([p1.copy(),p2.copy()])

        v1 = p1.pop(0)
        v2 = p2.pop(0)

        print("Player 1 plays:", v1)
        print("Player 2 plays:", v2)

        if (len(p1) + 1 > v1 and len(p2) + 1 > v2):
            print("Playing a sub-game to determine the winner...")
            subGame[0] += 1
            pwon, player = playGame2(p1[0:v1].copy(), p2[0:v2].copy(), subGame[0], subGame)

            if (player == "1"):
                p1.append(v1)
                p1.append(v2)
            else:
                p2.append(v2)
                p2.append(v1)

            print(f"The winner of game {subGame} is player {player}!")

            print(f"...anyway back to game {game}.")
            print(f"Player {player} wins round {turn} of game {game}!")
            #return (p1, "1") if len(p1) > 0 else (p2, "2")
        elif (v1 > v2):
            print(f"Player 2 wins round {turn} of game {game}!")
            p1.append(v1)
            p1.append(v2)
        else:
            print(f"Player 2 wins round {turn} of game {game}!")
            p2.append(v2)
            p2.append(v1)
        print()

    # for h in history[1]:
    #     print(h)

    return (p1, "1") if len(p1) > 0 else (p2, "2")

def part2():
    p1, p2 = readFile()
    pwon, player = playGame2(p1, p2)

    print("== Post-game results ==")
    print("Player 1's deck: ", p1)
    print("Player 2's deck: ", p2)

    score = 0
    if len(pwon) > 0:
        pwon = pwon[::-1]
        for i in range(1, len(pwon) + 1):
            score += (i * pwon[i-1])
    print(score)

#part1()
part2()