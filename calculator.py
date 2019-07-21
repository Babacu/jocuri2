def total(x, y):
    return x+y
def subtraction(x, y):
    return x-y
def multiplication(x, y):
    return x*y
def div(x, y):
    return x/y

loop = 1

alegere = 0

print("Buna ziua!")
# Say Hello
greeting = input()
print("Cum va numiti? ")
#Your name
name = input()
print(f"Buna {nume}, bine ai venit pe calculator.py")
print("Introdu doua valori: ")
# write 2 numbers
num1 = int(input())
num2 = int(input())
while loop == 1:
    # Choose which operation you want the computer to do
    print(" ")
    print("1) Adunare") #Is the sum of the numbers
    print("2) Scadere") #The subtraction of the numbers
    print("3) Inmultire") #The multiplication of the numbers
    print("4) Impartire") #The division of the numbers
    print("5) Nu sunt interesat") #You're not interested in what this app can do
    print(" ")
    print("Alegeti optiunea dorita: ")
    operation = int(input())
    if operation == 1:
        print("Suma celor doua numere este: ", total(num1, num2))
    elif operation == 2:
        print("Diferenta numerelor este: ", subtraction(num1, num2))
    elif operation == 3:
        print("Produsul numerelor este: ", multiplication(num1, num2))
    elif operation == 4:
        print(" Numarul ", num1, "impartit la ", num2, "este egal cu: ", div(num1, num2))
    elif operation == 5:
        # Leave the app
        print("Sunteti sigur ca dorit sa parasiti calculator.py? da sau nu?")
        leave = input()
        if leave == "da":
            loop = 0
        else:
            print("ok")
            continue
print("Va multumim ca ati folosit calculator.py")
