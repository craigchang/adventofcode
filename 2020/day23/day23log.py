
def printCups(currentCup, cups):
    print("cups: ", end="")
    for i in range(len(cups)):
        if (i == currentCup):
            print(f"({cups[i]})", "", end="")
        else:
            print(cups[i], "", end="")
    print()

def part1(cups, numMoves, part1 = True):
    move = 1
    currentCupIndex = 0
    while move <= numMoves:
        #print(f"-- move {move} --")
        currentCupIndex = currentCupIndex % len(cups)
        #printCups(currentCupIndex, cups)
        
        pickUp = []
        pickUpIndex = currentCupIndex
        for i in range(3):
            pickUpIndex = (pickUpIndex + 1) % len(cups)
            pickUp.append(cups[pickUpIndex])
        #print(f"pick up {pickUp}")

        destinationCup =  cups[currentCupIndex] - 1
        while destinationCup not in cups or destinationCup in pickUp: # chosen cup not in list or cup in pickup list
            if (min(cups) >= destinationCup):
                destinationCup = max(cups)
            else:
                destinationCup -= 1
        #print(f"destination: {destinationCup}")

        #destinationCupIndex = cups.index(destinationCup)

        tempCups = cups.copy()

        pickIndex1 = cups.index(pickUp[0])
        pickIndex2 = cups.index(pickUp[1])
        pickIndex3 = cups.index(pickUp[2])

        tempCups.remove(pickUp[0])
        tempCups.remove(pickUp[1])
        tempCups.remove(pickUp[2])

        di = tempCups.index(destinationCup)

        tempCups.insert(di + 1, pickUp[2])
        tempCups.insert(di + 1, pickUp[1])
        tempCups.insert(di + 1, pickUp[0])

        if (di < currentCupIndex):
            add = 0
            if (0 == pickIndex1):
                add -= 3
            elif (pickIndex1 > pickIndex2):
                add -= 2
            elif (pickIndex2 > pickIndex3):
                add -= 1

            for i in range(3 + add):
                val = tempCups.pop(0)
                tempCups.append(val)

        #print(tempCups)
        
        cups = tempCups.copy()
        currentCupIndex += 1
        move += 1
        if (move % 1 == 0):
            oneIndex = cups.index(1)
            print(move, oneIndex, cups[(oneIndex+1) % len(cups)], cups[(oneIndex+2) % len(cups)])

    # print("-- final --")
    # print(f"cups: {cups}")

    oneIndex = cups.index(1)

    #print(cups)
    
    if (part1): # part 1
        final = cups[oneIndex + 1: len(cups)] + cups[0:oneIndex]
        print("".join([str(x) for x in final]))
    else: # part 2
        print(cups.index(oneIndex+1), cups.index(oneIndex+2))
        print(cups.index(oneIndex+1) * cups.index(oneIndex+2))

#part1([int(x) for x in "389125467"], 100)
#part1([int(x) for x in "476138259"], 100)
part1([int(x) for x in "389125467"] + [x for x in range(10,1001,1)], 1600, False)
#part1([int(x) for x in "389125467"] + [x for x in range(10,1000001,1)], 10000000)
#part1([int(x) for x in "389125467"] + [x for x in range(10,10001,1)], 100000)
