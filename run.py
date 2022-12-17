import random
# set game
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "x"
winner = None
gameRunning = True
name = None
xScore = 0
oScore = 0


def intro():
    print()
    print("WELCOME TO TIC TAC TOE")
    print()
    print("------------------------------------------")
    print()
    print("GAME RULES")
    print('1: You are player x and the computer is player o.')
    print('2: First horizental row represents spot 1, 2 and 3')
    print('3: Second horizental row represents spot 4, 5 and 6')
    print('4: Third horizental row represents spot 7, 8 and 9')
    print('5: choose the number which matches your desired spot')
    print('6: To win game, match any 3 spots')
    print('vertically, horizentally or diagnally.')
    print("-----------------------------------------------")
    print()


def getUsername():
    global name
    """Get username and validate."""
    while True:
        name = input("To continue Enter your name please : ")
        print()
        if not name:
            print("Name cannot be empty! Try again")
        else:
            print('WELLCOME to tic tac toe ' + name + '')
            print('Choose spot in the board')
            print()
            break

# print game board


def printBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput():
    while True:
        try:
            inp = int(input("Its your turn, Select a spot from 1-9: "))
        except ValueError:
            print("wrong input, Please try again.")
            continue
        if inp <= 0 or inp >= 10:
            print('Not a valid choice, please enter a number between 1 and 9.')
            continue
        elif board[inp-1] == "o" or board[inp-1] == "x":
            print("opps, spot is occupied. Choose another spot.")
            continue
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
def checkTie():
    global board
    if "-" not in board:
        print('Game over. It is a tie.')
        return


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
        global name
        global xScore
        global oScore
        global currentPlayer
        print("-----------------------------------------------")
        print()
        print('GAMEOVER. ')
        currentPlayer = winner
        if winner == "x":
            xScore += 1
            print('The winner is ' + name + ' ')
            playAgainOrNot()
        elif winner == "o":
            oScore += 1
            print("The winner is player O")
            playAgainOrNot()
    return


def playAgainOrNot():
    global gameRunning
    while True:
        try:
           askUser = int(input("Thank you for playing !!, would you like to play again?, press 1 for yes. "))
        except ValueError:
            print("wrong input, Please try again.")
            continue
        if askUser != 1:
            print("wrong input, Please try again.")
            continue
        else:
            main()
            break


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
    intro()
    getUsername()
    printBoard()
    while gameRunning == True:
        playerInput()
        switchPlayer()
        computer(board)
        printBoard()
        checkwinner()
        checkTie()


main()


def quitAll():
    global gameRunning
    print()
    print("THANK YOU FOR PLAYING. GOODBYE.")
    gameRunning = False


quitAll()
