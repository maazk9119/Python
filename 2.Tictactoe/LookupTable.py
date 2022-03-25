import random

# This function prints out the board that it was passed.
# "board" is a list of 10 strings representing the board (ignore index 0)
def drawBoard(board):
    print("\n\n\n")
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# Lets the player type which letter they want to be.
# Returns a list with the player's letter as the first item, and the computer's letter as the second.
# For simplification, keeping X as the player's letter and 0 as the computer's letter
def inputPlayerLetter():
    return ['X', 'O']

# for simplification letteing the computer go first
def whoGoesFirst():
    return 'computer'

# This function returns True if the player wants to play again, otherwise it returns False.
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# Given a board and a player's letter, this function returns True if that player has won.
# We use bo instead of board and le instead of letter so we don't have to type as much.
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


# Make a duplicate of the board list and return it the duplicate.
def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def getPlayerMove(board):
    # Let the player type in his move.
    #while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
    #    print('What is your next move? (1-9)')
    #    move = input()

    move = 2
    if board[1] ==   'O' and board[2] == ' ' and board[3] == ' ' and board[4] == ' ' and board[5]== ' 'and board[6] == ' ' and board[7] == ' ' and board[8] == ' ' and board[9] == ' ':
        move = 5
    elif board[1] == ' ' and board[2] == ' ' and board[3] == 'O' and board[4] == ' ' and board[5]==' ' and board[6] == ' ' and board[7] == ' ' and board[8] == ' ' and board[9] == ' ':
        move = 5
    elif board[1] == ' ' and board[2] == ' ' and board[3] == ' ' and board[4] == ' ' and board[5]==' ' and board[6] == ' ' and board[7] == 'O' and board[8] == ' ' and board[9] == ' ':
        move = 7
    elif board[1] == ' ' and board[2] == ' ' and board[3] == ' ' and board[4] == ' ' and board[5]==' ' and board[6] == ' ' and board[7] == ' ' and board[8] == ' ' and board[9] == 'O':
        move = 5
    elif board[1] == ' ' and board[2] == ' ' and board[3] == ' ' and board[4] == ' ' and board[5]=='X' and board[6] == ' ' and board[7] == ' ' and board[8] == 'O' and board[9] == 'O':
        move = 7
    elif board[1] == ' ' and board[2] == ' ' and board[3] == ' ' and board[4] == ' ' and board[5]=='X' and board[6] == ' ' and board[7] == 'O' and board[8] == ' ' and board[9] == 'O':
        move = 8
    elif board[1] == ' ' and board[2] == ' ' and board[3] == ' ' and board[4] == ' ' and board[5]=='X' and board[6] == ' ' and board[7] == 'O' and board[8] == 'O' and board[9] == ' ':
        move = 9
    elif board[1] == ' ' and board[2] == ' ' and board[3] == ' ' and board[4] == ' ' and board[5]=='X' and board[6] == 'O' and board[7] == ' ' and board[8] == ' ' and board[9] == 'O':
        move = 3
    elif board[1] == ' ' and board[2] == ' ' and board[3] == ' ' and board[4] == ' ' and board[5]=='X' and board[6] == 'O' and board[7] == ' ' and board[8] == ' ' and board[9] == 'O':
        move = 3
    elif board[1] == ' ' and board[2] == ' ' and board[3] == ' ' and board[4] == ' ' and board[5]=='X' and board[6] == 'O' and board[7] == 'X' and board[8] == 'O' and board[9] == 'O':
        move = 3
    elif board[1] == ' ' and board[2] == ' ' and board[3] == ' ' and board[4] == ' ' and board[5]=='X' and board[6] == 'O' and board[7] == 'O' and board[8] == 'O' and board[9] == 'X':
        move = 3
    elif board[1] == ' ' and board[2] == ' ' and board[3] == 'O' and board[4] == 'O' and board[5]=='X' and board[6] == ' ' and board[7] == ' ' and board[8] == ' ' and board[9] == 'O':
        move = 7
    elif board[1] == ' ' and board[2] == ' ' and board[3] == 'O' and board[4] == 'O' and board[5]=='X' and board[6] == ' ' and board[7] == 'O' and board[8] == ' ' and board[9] == ' ':
        move = 1
    elif board[1] == ' ' and board[2] == ' ' and board[3] == 'O' and board[4] == 'O' and board[5]=='X' and board[6] == ' ' and board[7] == 'O' and board[8] == 'O' and board[9] == 'X':
        move = 1
   # elif board[1] == ' ' and board[2] == ' ' and board[3] == 'X' and board[4] == 'O' and board[5]=='X' and board[6] == 'O' and board[7] == ' ' and board[8] == ' ' and board[9] == 'O':
   # elif board[1] == ' ' and board[2] == ' ' and board[3] == 'O' and board[4] == ' ' and board[5]==' ' and board[6] == ' ' and board[7] == ' ' and board[8] == ' ' and board[9] == ' ':


    return move

# Returns a valid move from the passed list on the passed board.
# Returns None if there is no valid move.
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


# Return true if the passed move is free on the passed board.
def isSpaceFree(board, move):
    return board[move] == ' '


# This function simply marks the planned move (location of the borad) with the player's letter.
def makeMove(board, letter, move):
    board[move] = letter


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


# Return True if every space on the board has been taken. Otherwise return False.
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True



#=======================Drive Code===============================
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break












