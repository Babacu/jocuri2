# This function adds two numbers
def add(x, y):
    return x+y
# This function subtracts two numbers
def subtract(x, y):
    return x-y
# This function multiply two numbers
def multiply(x, y):
    return x*y
# This function divide two numbers
def divide(x, y):
    return x/y

loop = 1

alegere = 0

print("Buna ziua!")
# Welcoming the user
greeting = input()
print("Cum va numiti? ")
#Your name
name = input()
print(f"Buna {name}, bine ai venit pe calculator.py")
# write 2 numbers
num1 = int(input("Introdu primul numar: "))
num2 = int(input("Introdu al doilea numar: "))
while loop == 1:
    print(" ")
    print("1) Adunare") #Is the sum of the numbers
    print("2) Scadere") #The subtraction of the numbers
    print("3) Inmultire") #The multiplication of the numbers
    print("4) Impartire") #The division of the numbers
    print("5) Nu sunt interesat") #You're not interested in what this app can do
    print(" ")
    # Choose which operation you want the computer to do
    print("Alegeti optiunea dorita: ")
    operation = int(input())
    if operation == 1:
        print("Suma celor doua numere este: ", add(num1, num2))
    elif operation == 2:
        print("Diferenta numerelor este: ", subtract(num1, num2))
    elif operation == 3:
        print("Produsul numerelor este: ", multiply(num1, num2))
    elif operation == 4:
        print(" Numarul ", num1, "impartit la ", num2, "este egal cu: ", divide(num1, num2))
    elif operation == 5:
        # leave the app
        print("Sunteti sigur ca dorit sa parasiti calculator.py? da sau nu?")
        leave = input()
        if leave == "da":
            loop = 0
        else:
            print("ok")
            continue
print("Va multumim ca ati folosit calculator.py")
