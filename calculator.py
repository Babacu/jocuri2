def adunare(x, y):
    return x+y
def scadere(x, y):
    return x-y
def inmultire(x, y):
    return x*y
def impartire(x, y):
    return x/y

bucla = 1

alegere = 0

print("Buna ziua!")
salut = input()
print("Cum va numiti? ")
nume = input()
print(f"Buna {nume}, bine ai venit pe calculator.py")
print("Introdu doua valori: ")
a = int(input())
b = int(input())
while bucla == 1:
    print(" ")
    print("1) Adunare")
    print("2) Scadere")
    print("3) Inmultire")
    print("4) Impartire")
    print("5) Nu sunt interesat")
    print(" ")
    print("Alegeti optiunea dorita: ")
    alegere = int(input())
    if alegere == 1:
        print("Suma celor doua numere este: ", adunare(a, b))
    elif alegere == 2:
        print("Diferenta numerelor este: ", scadere(a, b))
    elif alegere == 3:
        print("Produsul numerelor este: ", inmultire(a, b))
    elif alegere == 4:
        print(" Numarul ", a, "impartit la ", b, "este egal cu: ", impartire(a, b))
    elif alegere == 5:
        print("Sunteti sigur ca dorit sa parasiti calculator.py? da sau nu?")
        dorinta = input()
        if dorinta == "da":
            bucla = 0
        else:
            print("ok")
            continue
print("Va multumim ca ati folosit calculator.py")
