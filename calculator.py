print("X si 0")
print(" ")

# the spaces bellow represent the position where the players will put x or 0 
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# This is the game board
def board():
    print(board[0], ' |', board[1], '|', board[2])
    print('___|___|___')
    print(board[3], ' |', board[4], '|', board[5])
    print('___|___|___')
    print(board[6], ' |', board[7], '|', board[8])
    print('   |   |   ')
    print(" ")
# These are the two lists which contains the position of x and 0
positionsOfX = ["x,1", "x,2", "x,3", "x,4", "x,5", "x,6", "x,7", "x,8", "x,9"]
positionsOf0 = ["0,1", "0,2", "0,3", "0,4", "0,5", "0,6", "0,7", "0,8", "0,9"]

tabla()

loop = 1
while loop == 1:
    loop2 = 1
    loop3 = 1
    while loop2 == 1:
        # Is the first player's turn
        print("Randul lui x")
        #The first player decides in which position he will place x
        positionOfX = input()
        if positionOfX == positionsOfX[0]:
            board[0] = "x"
        elif positionOfX == positionsOfX[1]:
            board[1] = "x"
        elif positionOfX == positionsOfX[2]:
            board[2] = "x"
        elif positionOfX == positionsOfX[3]:
            board[3] = "x"
        elif positionOfX == positionsOfX[4]:
            board[4] = "x"
        elif positionOfX == positionsOfX[5]:
            board[5] = "x"
        elif positionOfX == positionsOfX[6]:
            board[6] = "x"
        elif positionOfX == positionsOfX[7]:
            board[7] = "x"
        elif positionOfX == positionsOfX[8]:
            board[8] = "x"
        else:
            # type one position from 1 to 9, not other ones
            print("Nu inteleg ce doriti sa scrieti!")
            print("Va rugam, incercati din nou!")
            # please, insert the position again
            continue
        board()
        if "x" == board[0] and board[0] == board[1] and board[1] == board[2]:
            loop3 = 0
            loop = 0
            print("x a castigat")
        elif "x" == board[2] and board[2] == board[5] and board[5] == board[8]:
            loop3 = 0
            loop = 0
            print("x a castigat")
        elif "x" == board[6] and board[6] == board[7] and board[7] == board[8]:
            loop3 = 0
            loop = 0
            print("x a castigat")
        elif "x" == board[0] and board[0] == board[3] and board[3] == board[6]:
            loop3 = 0
            loop = 0
            print("x a castigat")
        elif "x" == board[0] and board[0] == board[4] and board[4] == board[8]:
            loop3 = 0
            loop = 0
            print("x a castigat")
        elif "x" == board[2] and board[2] == board[4] and board[4] == board[6]:
            loop3 = 0
            loop = 0
            print("x a castigat")
        elif "x" == board[1] and board[1] == board[4] and board[4] == board[7]:
            loop3 = 0
            loop = 0
            print("x a castigat")
        elif "x" == board[3] and board[3] == board[4] and board[4] == board[5]:
            loop3 = 0
            loop = 0
            print("x a castigat")
        loop2 = 0
    while loop3 == 1:
        print("Randul lui 0")
        #Now it's second player's turn who decides where to place 0
        positionOfZero = input()
        if positionOfZero == positionsOf0[0]:
            board[0] = "0"
        elif positionOfZero == positionsOf0[1]:
            board[1] = "0"
        elif positionOfZero == positionsOf0[2]:
            board[2] = "0"
        elif positionOfZero == positionsOf0[3]:
            board[3] = "0"
        elif positionOfZero == positionsOf0[4]:
            board[4] = "0"
        elif positionOfZero == positionsOf0[5]:
            board[5] = "0"
        elif positionOfZero == positionsOf0[6]:
            board[6] = "0"
        elif positionOfZero == positionsOf0[7]:
            board[7] = "0"
        elif positionOfZero == positionsOf0[8]:
             board[8] = "0"
        else:
            print("Nu inteleg ce vreti sa scrieti!")
            print("Va rugam, incercati din nou!")
            continue
        board()
        if "0" == board[0] and board[0] == board[1] and board[1] == board[2]:
            loop = 0
            print("0 a castigat")
        elif "0" == board[2] and board[2] == board[5] and board[5] == board[8]:
            loop = 0
            print("0 a castigat")
        elif "0" == board[6] and board[6] == board[7] and board[7] == board[8]:
            loop = 0
            print("0 a castigat")
        elif "0" == board[0] and board[0] == board[3] and board[3] == board[6]:
            loop = 0
            print("0 a castigat")
        elif "0" == board[0] and board[0] == board[4] and board[4] == board[8]:
            loop = 0
            print("0 a castigat")
        elif "0" == board[2] and board[2] == board[4] and board[4] == board[6]:
            loop = 0
            print("0 a castigat")
        elif "0" == board[1] and board[1] == board[4] and board[4] == board[7]:
            loop = 0
            print("0 a castigat")
        elif "0" == board[3] and board[3] == board[4] and board[4] == board[5]:
            loop = 0
            print("0 a castigat")
        loop3 = 0
print("Va multumim!")
