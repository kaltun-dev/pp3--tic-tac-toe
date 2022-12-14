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
     print(board[3] + " | " + board[4] + " | " + board[5])
     print(board[6] + " | " + board[7] + " | " + board[8])

printBoard()

# take player input
# check for win or tie
# switch player
# check for win or tie again
# swich the player 
# check for win or tie again.

