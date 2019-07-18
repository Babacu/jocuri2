print("X si 0")
print(" ")

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def tabla():
    print(board[0], ' |', board[1], '|', board[2])
    print('___|___|___')
    print(board[3], ' |', board[4], '|', board[5])
    print('___|___|___')
    print(board[6], ' |', board[7], '|', board[8])
    print('   |   |   ')
    print(" ")

tabla()

loop = 1
while loop == 1:
    loop2 = 1
    loop3 = 1
    while loop2 == 1:
        print("Randul lui x")
        alegere_x = input()
        if alegere_x == "x,1" or alegere_x == "x, 1":
            board[0] = "x"
        elif alegere_x == "x,2" or alegere_x == "x, 2":
            board[1] = "x"
        elif alegere_x == "x,3" or alegere_x == "x, 3":
            board[2] = "x"
        elif alegere_x == "x,4" or alegere_x == "x, 4":
            board[3] = "x"
        elif alegere_x == "x,5" or alegere_x == "x, 5":
            board[4] = "x"
        elif alegere_x == "x,6" or alegere_x == "x, 6":
            board[5] = "x"
        elif alegere_x == "x,7" or alegere_x == "x, 7":
            board[6] = "x"
        elif alegere_x == "x,8" or alegere_x == "x, 8":
            board[7] = "x"
        elif alegere_x == "x,9" or alegere_x == "x, 9":
            board[8] = "x"
        else:
            print("Nu inteleg ce doriti sa scrieti!")
            print("Va rugam, incercati din nou!")
            continue
        tabla()
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
        alegere_0 = input()
        if alegere_0 == "0,1" or alegere_0 == "0, 1":
            board[0] = "0"
        elif alegere_0 == "0,2" or alegere_0 == "0, 2":
            board[1] = "0"
        elif alegere_0 == "0,3" or alegere_0 == "0, 3":
            board[2] = "0"
        elif alegere_0 == "0,4" or alegere_0 == "0, 4":
            board[3] = "0"
        elif alegere_0 == "0,5" or alegere_0 == "0, 5":
            board[4] = "0"
        elif alegere_0 == "0,6" or alegere_0 == "0, 6":
            board[5] = "0"
        elif alegere_0 == "0,7" or alegere_0 == "0, 7":
            board[6] = "0"
        elif alegere_0 == "0,8" or alegere_0 == "0, 8":
            board[7] = "0"
        elif alegere_0 == "0,9" or alegere_0 == "0, 9":
             board[8] = "0"
        else:
            print("Nu inteleg ce vreti sa scrieti!")
            print("Va rugam, incercati din nou!")
            continue
        tabla()
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
