import numpy as np

def get_input():    
    with open("./day15/input.txt") as f:
        input_ = list(map(lambda x: x.rstrip(), f.readlines()))
        return( [ [int(c) for c in r] for r in input_ ] )    
    
def precompute(board,costboard):

    #initialize
    change=1
    for i,x in np.ndenumerate(board):
        #print(i,x)
        if (i[0] == 0 and i[1] == 0):
            continue
        elif (i[0]==0):
            costboard[i] = costboard[(0,i[1]-1)] + x
        elif (i[1]==0):
            costboard[i] = costboard[(i[0]-1,0)] + x
        else:
            costboard[i] = min([ costboard[(i[0],i[1]-1)],costboard[(i[0]-1,i[1])] ]) + x
            
   #process         
    while(change):
        #do 2 passes through the array (bottom right -> upper left and then return )
        change = 0

        board = np.flip(np.flip(board,0),1)
        costboard = np.flip(np.flip(costboard,0),1)

        costboard,change = optimize(board,costboard,change)
        
        board = np.flip(np.flip(board,0),1)
        costboard = np.flip(np.flip(costboard,0),1)
        
        costboard,change = optimize(board,costboard,change)

    return(costboard)

def optimize(board,costboard,change):

        for i,x in np.ndenumerate(board):       
            if (i[0] == 0 and i[1] == 0):
                continue
            elif (i[0]==0):
                if costboard[i] > costboard[(0,i[1]-1)] + x:
                    change+=1
                    costboard[i] = costboard[(0,i[1]-1)] + x
            elif (i[1]==0):
                if costboard[i] > costboard[(i[0]-1,0)] + x:
                    change+=1
                    costboard[i] = costboard[(i[0]-1,0)] + x
            else:
                if costboard[i] > min([ costboard[(i[0],i[1]-1)],costboard[(i[0]-1,i[1])] ]) + x:
                    change+=1
                    costboard[i] = min([ costboard[(i[0],i[1]-1)],costboard[(i[0]-1,i[1])] ]) + x
        return(costboard,change)    
    
def main():

    input_ = get_input()

    board = np.array(input_)
    costboard  = np.full(board.shape,2**31,dtype=int)
    start = (0,0)
    costboard[start] = 0
 
    costboard = precompute(board,costboard)
    
    answer1 = costboard.flat[-1]   
    
    #part2
    ey,ex = 5,5
    my,mx = board.shape
    
    p2board = np.zeros((my*ey,mx*ex), dtype=int)
    for p2y in range(ex):
        p2row = []
        for p2x in range(ey):
            for y in range(my):
                for x in range(mx):
                    p2board[ y+my*p2y, x+mx*p2x ] = board[y,x]+p2x+p2y
    
    p2board[p2board > 9] += 1   #would break if value > 18
    p2board[p2board > 9] %= 10
    
    costboard  = np.full(p2board.shape,2**31,dtype=int)
    costboard[start] = 0
    
    costboard = precompute(p2board,costboard)
    
    answer2 = costboard.flat[-1]

    return(answer1,answer2)

print(main())