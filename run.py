
# introduction to game
# set game
board = [ "-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

CurrentPlayer = "x"
winner = None
gameRunning = True

# print game board


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# take player input
# check for win or tie
# switch player
# check for win or tie again
# swich the player 
# check for win or tie again.

