import random
# set game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "x"
winner = None
gameRunning = True

def getUsername():
    """Get username and validate."""
    while True:
        name = input("Enter your name: ")
        if not name:
            print("Name cannot be empty! Try again")
        else:
            print( 'WELLCOME to tic tac toe ' + name + ' place X on board')
            print( 'To win, match 3 slots vertically horizentally or diagnally. ')
            print("-----------------------------------------------")
            break

# print game board
def printBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput():
        #Get player choice.
    while True:
        try:
            inp = int(input("Select a spot 1-9: "))
        except ValueError:
            print("wrong input, Please try again.")
            continue
        if inp <= 0 or inp >= 10:
            print('Not a valid choice, please enter a number between 1 and 9.')
            continue
        elif board[inp-1] == "o" or board[inp-1] == "x":
            print("opps, spot is occupied. Choose another spot.")
        else:
            board[inp-1] == "-"
            board[inp-1] = currentPlayer
            break

# check for win or on different positions
def checkHorizontleRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkVerticalRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True


def checkDiagnalRow(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


# check for tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard()
        print('Game over. It is a tie.')
        print("Thank you for playing GoodBye.")
        gameRunning == False


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"


# check for win
def checkwinner():
    if checkHorizontleRow(board) or checkVerticalRow(board) or checkDiagnalRow(board):
        global gameRunning
        #print(f"the winner is {winner}")
        print("-----------------------------------------------")
        printBoard()
        print(f"the winner is {winner}")
        askUser = input("Thank you for playing !!, would you like to play again?, press y for yes, n for no. ")
        if askUser == "y":
            #gameRunning = True
            main()
        elif askUser == "n":
            print("Thank you for playing , Goodbye.")
            gameRunning = False

# play against computer
def computer(board):
    while currentPlayer == "o":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "o"
            switchPlayer()


def main():
    global board
    board = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
    getUsername()
    printBoard()
    while gameRunning == True:
        playerInput()
        switchPlayer()
        computer(board)
        printBoard()
        checkwinner()
        checkTie(board)


main()
