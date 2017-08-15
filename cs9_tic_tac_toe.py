import random

def createBoard():
    return [0,0,0, \
            0,0,0, \
            0,0,0]
			
def checkPattern(player, board, move):

    """
    Blocking
    the player

    Checking all areas of the board for
    available blocking move. Either to win or
    block the player.
    """
    
    #Horizontals
    if (board[0] == player and board[1] == player):
        if board[2] != move and board[2] != player:
            return [True,2]
        
    if board[1] == player and board[2] == player:
        if board[0] != move and board[0] != player:
            return [True,0]
    
    if board[3] == player and board[4] == player:
        if board[5] != move and board[5] != player:
            return [True,5]
        
    if board[4] == player and board[5] == player:
        if board[3] != move and board[3] != player:
            return [True,3] 
    
    if board[6] == player and board[7] == player:
        if  board[8] != move and board[8] != player:
            return [True,8]

    if board[7] == player and board[8] == player:
        if board[6] != move and board[6] != player:
            return [True,6]

    #Verticals
    if board[0] == player and board[3] == player:
        if board[6] != move and board[6] != player:
            return [True,6]

    if board[3] == player and board[6] == player:
        if board[0] != move and board[0] != player:
            return [True,0]

    if board[1] == player and board[4] == player:
        if board[7] != move and board[7] != player:
            return [True,7]
        
    if board[4] == player and board[7] == player:
        if board[1] != move and board[1] != player:
            return [True,1]

    if board[2] == player and board[5] == player:
        if board[8] != move and board[8] != player:
            return [True,8]
        
    if board[5] == player and board[8] == player:
        if board[2] != move and board[2] != player:
            return [True,2]

    #Diagonals
    if board[0] == player and board[4] == player:
        if board[8] != move and board[8] != player:
            return [True,8]
        
    if board[4] == player and board[8] == player:
        if board[0] != move and board[0] != player:
            return [True,0]

    if board[2] == player and board[4] == player:
        if board[6] != move and board[6] != player:
            return [True,6]
        
    if board[4] == player and board[6] == player:
        if board[2] != move and board[2] != player:
            return [True,2]

    #0 1 2
    #3 4 5 //Display 
    #6 7 8
    #Middle Blocks e.g => X--O--X
    #Horizontals
    if board[0] == player and board[2] == player:
        if board[1] != move and board[1] != player:
            return [True, 1]

    if board[3] == player and board[5] == player:
        if board[4] != move and board[4] != player:
            return [True, 4]

    if board[6] == player and board[8] == player:
        if board[7] != move and board[7] != player:
            return [True, 7]

    #Verticals
    if board[0] == player and board[6] == player:
        if board[3] != move and board[3] != player:
            return [True, 3]

    if board[1] == player and board[7] == player:
        if board[4] != move and board[4] != player:
            return [True, 4]

    if board[2] == player and board[8] == player:
        if board[5] != move and board[5] != player:
            return [True, 5]

    #Diagonals
    if board[0] == player and board[8] == player:
        if board[4] != move and board[4] != player:
            return [True, 4]

    if board[2] == player and board[6] == player:
        if board[4] != move and board[4] != player:
            return [True, 4]   


    """
    Winning
    the player
    """
    
    #Horizontals
    if (board[0] == move and board[1] == move):
        if board[2] != move and board[2] != player:
            return [True,2]
        
    if board[1] == move and board[2] == move:
        if board[0] != move and board[0] != player:
            return [True,0]
    
    if board[3] == move and board[4] == move:
        if board[5] != move and board[5] != player:
            return [True,5]
        
    if board[4] == move and board[5] == move:
        if board[3] != move and board[3] != player:
            return [True,3] 
    
    if board[6] == move and board[7] == move:
        if  board[8] != move and board[8] != player:
            return [True,8]

    if board[7] == move and board[8] == move:
        if board[6] != move and board[6] != player:
            return [True,6]

    #Verticals
    if board[0] == move and board[3] == move:
        if board[6] != move and board[6] != player:
            return [True,6]

    if board[3] == move and board[6] == move:
        if board[0] != move and board[0] != player:
            return [True,0]

    if board[1] == move and board[4] == move:
        if board[7] != move and board[7] != player:
            return [True,7]
        
    if board[4] == move and board[7] == move:
        if board[1] != move and board[1] != player:
            return [True,1]

    if board[2] == move and board[5] == move:
        if board[8] != move and board[8] != player:
            return [True,8]
        
    if board[5] == move and board[8] == move:
        if board[2] != move and board[2] != player:
            return [True,2]

    #Diagonals
    if board[0] == move and board[4] == move:
        if board[8] != move and board[8] != player:
            return [True,8]
        
    if board[4] == move and board[8] == move:
        if board[0] != move and board[0] != player:
            return [True,0]

    if board[2] == move and board[4] == move:
        if board[6] != move and board[6] != player:
            return [True,6]
        
    if board[4] == move and board[6] == move:
        if board[2] != move and board[2] != player:
            return [True,2]

    #Middle Winning Blocks
     #Horizontals
    if board[0] == move and board[2] == move:
        if board[1] != move and board[1] != player:
            return [True, 1]

    if board[3] == move and board[5] == move:
        if board[4] != move and board[4] != player:
            return [True, 4]

    if board[6] == move and board[8] == move:
        if board[7] != move and board[7] != player:
            return [True, 7]

    #Verticals
    if board[0] == move and board[6] == move:
        if board[3] != move and board[3] != player:
            return [True, 3]

    if board[1] == move and board[7] == move:
        if board[4] != move and board[4] != player:
            return [True, 4]

    if board[2] == move and board[8] == move:
        if board[5] != move and board[5] != player:
            return [True, 5]

    #Diagonals
    if board[0] == move and board[8] == move:
        if board[4] != move and board[4] != player:
            return [True, 4]

    if board[2] == move and board[6] == move:
        if board[4] != move and board[4] != player:
            return [True, 4]
    


def botMove(move, board, player):

    blockStrategy = checkPattern(player, board, move)
    if blockStrategy != None and blockStrategy[0] == True:
        print blockStrategy
        if board[blockStrategy[1]] == move: 
            print "Move 0"
        else:
            board[blockStrategy[1]] = move
    
    elif board.index(player)-1 == 0 and board[board.index(player)-1] == 0:
        index = board.index(player)-1
        board[index] = move
        print "Move 1"
    
    elif board.index(player)+1 == 0 and board[board.index(player)+1] == 0:
        index = board.index(player)+1
        board[index] = move
        print "Move 2"

    else:
        pos = random.randint(1,9)
        while True:
            pos = random.randint(1,9)
            if board[pos-1] == 0:
                board[pos-1] = move
                print "Move 3"
                break
            
        
                
                

def display(board):
    """
    Display board in
    a proper format
    for the user
    """
    print   str(board[0]) + " " + str(board[1]) + " " + str(board[2]) + "\n" +\
            str(board[3]) + " " + str(board[4]) + " " + str(board[5]) + "\n" +\
            str(board[6]) + " " + str(board[7]) + " " + str(board[8]) + "\n"


def check(board, bot, player):
    """
    Check board of tripples. If a tripple
    has occured, appoint a winner.
    """
    winP = False
    winB = False

    #Horizontal Lines
    if board[0] == player and board[1] == player and board[2] == player:
        winP = True
    elif board[0] == bot and board[1] == bot and board[2] == bot:
        winB = True
        
    elif board[3] == player and board[4] == player and board[5] == player:
        winP = True
    elif board[3] == bot and board[4] == bot and board[5] == bot:
        winB = True

    elif board[6] == player and board[7] == player and board[8] == player:
        winP = True
    elif board[6] == bot and board[7] == bot and board[8] == bot:
        winB = True

    #Vertical Lines
    elif board[0] == player and board[3] == player and board[6] == player:
        winP = True
    elif board[0] == bot and board[3] == bot and board[6] == bot:
        winB = True
        
    elif board[1] == player and board[4] == player and board[7] == player:
        winP = True
    elif board[1] == bot and board[4] == bot and board[7] == bot:
        winB = True

    elif board[2] == player and board[5] == player and board[8] == player:
        winP = True
    elif board[2] == bot and board[5] == bot and board[8] == bot:
        winB = True


    #Diagonals
    elif board[0] == player and board[4] == player and board[8] == player:
        winP = True
    elif board[0] == bot and board[4] == bot and board[8] == bot:
        winB = True
        
    elif board[2] == player and board[4] == player and board[6] == player:
        winP = True
    elif board[2] == bot and board[4] == bot and board[6] == bot:
        winB = True


    if winP == True:
        print str(player) + " wins!"
        main()
    elif winB == True:
        print str(bot) + " wins!"
        main()



def findEmptySpot(board, bot, player):
    """
    Check for empty spot
    and return the index for
    the bot move.
    """
    for item in board:
        if item != bot and item != player:
            return board.index(item)
            break

    
#0 1 2 //
#3 4 5 //Indexes
#6 7 8 //
def main():
    board = createBoard() #Create board


    #Choose Xs or Os
    choice = raw_input("Choose X or O: ")
    while choice not in 'xXoO':
        choice = raw_input("Choose X or O: ")


    #Appoint bots type according player
    if choice == 'X' or choice == 'x':
        bot = 'O'
    elif choice == 'O' or choice == 'o':
        bot = 'X'


    #Main loop app
    counter = 0

    while True:
        """
        Show debugging counter
        and assign moves
        """
        print "Counter: " + str(counter)
        if counter == 8:
            getSpot = findEmptySpot(board,bot,choice)
            board[getSpot] = bot
            check(board,bot,choice)
            again = raw_input("Play again?(Y/N): ")
            if again == "y" or again == "Y":
                main()
            elif again == "n" or again == "N":
                print "Thanks for playing!"
                break
            
        else:
            pos = input("Choose position (1-9): ")
            if board[pos-1] != bot:
                board[pos-1] = choice
                botMove(bot,board,choice)
                check(board,bot,choice)
                display(board)
                counter = counter + 2
            else:
                print "You can't play there."
                display(board)
    

#Starting the game
main()       
