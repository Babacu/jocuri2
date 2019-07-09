print('X si 0 -> 2 jucatori reali')
print('')

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def tabla():
    #print(' %c | %c | %c ' % (board[1], board[2], board[3]))
    print(board[0], ' |', board[1], '|', board[2])
    print('___|___|___')
    print(board[3], ' |', board[4], '|', board[5])
    print('___|___|___')
    print(board[6], ' |', board[7], '|', board[8])
    print('   |   |   ')
    print('')
def castigator_x():
    if "x" == board[0] and board[0] == board[1] and board[1] == board[2]:
        print("x a castigat")
    elif "x" == board[2] and board[2] == board[5] and board[5] == board[8]:
        print("x a castigat")
    elif "x" == board[6] and board[6] == board[7] and board[7] == board[8]:
        print("x a castigat")
    elif "x" == board[0] and board[0] == board[3] and board[3] == board[6]:
        print("x a castigat")
    elif "x" == board[0] and board[0] == board[4] and board[4] == board[8]:
        print("x a castigat")
    elif "x" == board[2] and board[2] == board[4] and board[4] == board[6]:
        print("x a castigat")
    elif "x" == board[1] and board[1] == board[4] and board[4] == board[7]:
        print("x a castigat")
    elif "x" == board[3] and board[3] == board[4] and board[4] == board[5]:
        print("x a castigat")
        
def castigator_0():
    if "0" == board[0] and board[0] == board[1] and board[1] == board[2]:
        print("0 a castigat")
    elif "0" == board[2] and board[2] == board[5] and board[5] == board[8]:
        print("0 a castigat")
    elif "0" == board[6] and board[6] == board[7] and board[7] == board[8]:
        print("0 a castigat")
    elif "0" == board[0] and board[0] == board[3] and board[3] == board[6]:
        print("0 a castigat")
    elif "0" == board[0] and board[0] == board[4] and board[4] == board[8]:
        print("0 a castigat")
    elif "0" == board[2] and board[2] == board[4] and board[4] == board[6]:
        print("0 a castigat")
    elif "0" == board[1] and board[1] == board[4] and board[4] == board[7]:
        print("0 a castigat")
    elif "0" == board[3] and board[3] == board[4] and board[4] == board[5]:
        print("0 a castigat")
    
tabla()

bucla = 1
while bucla == 1:
    print("Randul lui x")
    alegere_x = input()
    if alegere_x == "x,1":
        board[0] = "x"
        tabla()
        if "x" == board[0] and board[0] == board[1] and board[1] == board[2]:
            break
    elif alegere_x == "x,2":
        board[1] = "x"
        tabla()
        castigator_x()
    elif alegere_x == "x,3":
        board[2] = "x"
        tabla()
        castigator_x()
    elif alegere_x == "x,4":
        board[3] = "x"
        tabla()
        castigator_x()
    elif alegere_x == "x,5":
        board[4] = "x"
        tabla()
        castigator_x()
    elif alegere_x == "x,6":
        board[5] = "x"
        tabla()
        castigator_x()
    elif alegere_x == "x,7":
        board[6] = "x"
        tabla()
        castigator_x()
    elif alegere_x == "x,8":
        board[7] = "x"
        tabla()
        castigator_x()
    elif alegere_x == "x,9":
        board[8] = "x"
        tabla()
        castigator_x()
        
    print("Randul lui 0")

    alegere_0 = input()

    if alegere_0 == "0,1":
        board[0] = "0"
        tabla()
        castigator_0()
    elif alegere_0 == "0,2":
        board[1] = "0"
        tabla()
        castigator_0()
    elif alegere_0 == "0,3":
        board[2] = "0"
        tabla()
        castigator_0()
    elif alegere_0 == "0,4":
        board[3] = "0"
        tabla()
        castigator_0()
    elif alegere_0 == "0,5":
        board[4] = "0"
        tabla()
        castigator_0()
    elif alegere_0 == "0,6":
        board[5] = "0"
        tabla()
        castigator_0()
    elif alegere_0 == "0,7":
        board[6] = "0"
        tabla()
        castigator_0()
    elif alegere_0 == "0,8":
        board[7] = "0"
        tabla()
        castigator_0()
    elif alegere_0 == "0,9":
        board[8] = "0"
        tabla()
        castigator_0()
print("da")
