# set game
board = [ "-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

CurrentPlayer = "x"
winner = None
gameRunning = True

# introduction to game
name = input("Enter your name: ")
print( 'WELLCOME to tic tac toe ' + name + ' place X on board') 
print( 'To win, match 3 slots vertically horizentally or diagnally. ')

# print game board
def printBoard():
     print(board[0] + " | " + board[1] + " | " + board[2])
     print("____________")
     print(board[3] + " | " + board[4] + " | " + board[5])
     print("____________")
     print(board[6] + " | " + board[7] + " | " + board[8])

printBoard()

# take player input
def CurrentPlayerChooses(board):
     xInput = int(input("please enter a number from 1 - 9: "))
     if xInput >= 1 and xInput <= 9 and board[xinput-1] == "-":
          board[xInput-1] = CurrentPlayer
     else: 
          print("sorry, spot is occupied.") 


CurrentPlayerChooses(board)


# check for win or tie
# switch player
# check for win or tie again
# swich the player 
# check for win or tie again.
# startgame function 
# clear game function
