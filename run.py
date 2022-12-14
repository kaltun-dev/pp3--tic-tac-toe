
# set game
board = [ "-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "x"
winner = None
gameRunning = True
playerOScore = 0
playerXScore = 0

# introduction to game
"""name = input("Enter your name: ")
print( 'WELLCOME to tic tac toe ' + name + ' place X on board') 
print( 'To win, match 3 slots vertically horizentally or diagnally. ')
"""
# print game board
def printBoard():
     print(board[0] + " | " + board[1] + " | " + board[2])
     print("____________")
     print(board[3] + " | " + board[4] + " | " + board[5])
     print("____________")
     print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already at that spot.")


# check for win or tie
def checkHorizentalRow(board):
     global winner 
     if board[0] == board[1] == board[2] and board[1] != "-":
          winner = board[0]
          return True
     elif board[3] == board[4] == board[5] and board[3] != "-":
          winner = board[3]
          return True
     elif board[6] == board[7] == board[8] and board[6] != "-":
          winner = board[6]
          return True

def checkVerticalRow(board):
     if board[0] == board[3] == board[6] and board[0] != "-":
          winner = board[0]
          return True
     elif board[1] == board[4] == board[7] and board[1] != "-":
          winner = board[1]
          return True
     elif board[2] == board[5] == board[8] and board[2] != "-":
          winner = board[2]
          return True

def checkDiagnalRow(board):
     if board[0] == board[4] == board[8] and board[0] != "-":
          winner = board[0]
          return True
     elif board[2] == board[4] == board[6] and board[2] != "-":
          winner = board[2]
          return True

# check for win or tie


# switch player
# check for win or tie again
# swich the player 
# check for win or tie again.
# startgame function 
# clear game function

while gameRunning:
     printBoard()
     playerInput(board)

