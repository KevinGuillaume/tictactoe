
#Tic Tac Toe Game

board = [ ' ' for x in range(10)]

def placeLetter(letter,pos):
    board[pos] = letter

def openSpace(pos):
    return board[pos] == ' '

def printBoard(board):
    # Making the board out of text
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(brd, let):
    return (brd[7]==let and brd[8]== let and brd[9]==let) or (brd[4] == let and brd[5] == let and brd[6]==let) or (brd[1] == let and brd[2] == let and brd[3]==let) or (brd[1] == let and brd[4] == let and brd[7]==let) or (brd[2] == let and brd[5] == let and brd[8]==let) or (brd[3] == let and brd[6] == let and brd[9]==let) or (brd[1] == let and brd[5] == let and brd[9]==let) or (brd[3] == let and brd[5] == let and brd[7]==let) 
    

def playerMove():
    run = True
    while run:
        move = input("Pick a position for your \'X\' (1-9):")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if openSpace(move):
                    run = False
                    placeLetter('X', move)
                else:
                    print("Sorry, this space is taken!")
            else:
                print("Please enter a number within the range!")
        except:
            print("Please type a number!")
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy,let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print("TIME TO PLAY TIC TAC TOE!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O\'s wom this time!")
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print("Tie game")
            else:
                placeLetter('O',move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print("You won, nice!")
            break

    if isBoardFull(board):
        print("Tie Game!")

main()