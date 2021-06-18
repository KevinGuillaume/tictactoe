
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
    #Finding all ways for a winner to be possible 
    #First 3 rows horizontal,next 3 vetical, last two diagonal
    return (brd[7]==let and bo[8]== le and bo[9]==le) or
    (bo[4] == let and bo[5] == let and bo[6]==let) or
    (bo[1] == let and bo[2] == let and bo[3]==let) or
    (brd[1]==let and bo[4]== le and bo[7]==le) or
    (bo[2] == let and bo[5] == let and bo[8]==let) or
    (bo[3] == let and bo[6] == let and bo[9]==let) or
    (brd[1]==let and bo[5]== le and bo[9]==le) or
    (bo[3] == let and bo[5] == let and bo[7]==let) 
    

def playerMove():
    pass

def compMove():
    pass

def selectRandom(board):
    pass

def isBoardFull(board):
    pass

def main():
    pass

 main()