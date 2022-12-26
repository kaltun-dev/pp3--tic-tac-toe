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


# introduction to game
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


# gets user's name and saves it
def getUsername():
    global name
    """Get username and validate."""
    while True:
        name = input("To continue Enter your name please : \n")
        print()
        if not name:
            print("Name cannot be empty! Try again")
        else:
            print('WELLCOME to tic tac toe ' + name + '')
            print('Choose spot in the board')
            print()
            break


# prints board to terminal.
def printBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])


# gets player input and prints on board
def playerInput():
    while True:
        try:
            inp = int(input("Its your turn, Select a spot from 1-9: \n"))
        except ValueError:
            print("wrong input, Please try again.")
            continue
        if inp <= 0 or inp >= 10:
            print('Not a valid choice, please enter a number between 1 and 9.')
            continue
        elif board[inp-1] == "o" or board[inp-1] == "x":
            print("opps, spot is occupied. Choose another spot.")
            continue
        elif board[inp-1] == "-":
            board[inp-1] = currentPlayer
            break
        return


# check for win or on 8 diffrent positions in the board.
def checkWinnerOn8Positions(board):
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
    elif board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


# check for tie between 2 players
def checkTie():
    global board
    global winner
    if "-" not in board:
        print('Game over. It is a tie.')
        playAgainOrNot()
    return


# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"
    return


# check for win in either player.
def checkwinner():
    if checkWinnerOn8Positions(board):
        global name
        global currentPlayer
        print("-----------------------------------------------")
        print()
        printBoard()
        print()
        print('GAMEOVER. ')
        currentPlayer = winner
        if winner == "x":
            print('The winner is ' + name + ' ')
            playAgainOrNot()
        elif winner == "o":
            print("The winner is player O")
            playAgainOrNot()
        else:
            return


# option to play again or to stop.
def playAgainOrNot():
    global gameRunning
    while True:
        try:
            print("Thank you for playing, would you like to play again?")
            askUser = int(input("press 1 for yes or 2 for no: \n"))
        except ValueError:
            print("wrong input, Please try again.")
            continue
        if askUser != 1 and askUser != 2:
            print("wrong input, Please try again.")
            continue
        elif askUser == 1:
            currentPlayer = "x"
            main()
        elif askUser == 2:
            print()
            print("THANK YOU FOR PLAYING. GOODBYE.")
            quit()
            break
        return


# play against computer
def computer(board):
    global currentPlayer
    while currentPlayer == "o":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "o"
            checkwinner()
            checkTie()
            switchPlayer()


# Starts the game and resets the game.
def main():
    global board
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    currentPlayer = "x"
    intro()
    getUsername()
    printBoard()
    while gameRunning == True:
        playerInput()
        checkwinner()
        checkTie()
        switchPlayer()
        computer(board)
        printBoard()


# calling for game to start
main()
