def nume_persoane(x):
    return str(x)
def nume_persoana(y):
    return str(y)

bucla = 1
bucla2 = 1
print("Buna ziua")
salut = input()
print("Bine ati venit in agenda telefonica calculatorului")
agenda_telefonica = {"Sebi" : 770421464, "Balau" : 748113188, "Bianca" : 768152514,
                     "Crisan" : 724248152}
print("Doriti sa accesati contactele noastre")
dorinta = input()
if dorinta == "da":
    print("Contactele noastre sunt: ", agenda_telefonica.keys())
    print("Pe cine doriti sa cautati in agenda?")
    nume = input()
    if nume_persoane(nume) in agenda_telefonica:
        print("Numarul sau este", agenda_telefonica[nume_persoane(nume)])
        while bucla == 1:
            print("Vreti sa adaugati contacte noi in agenda? ")
            dorinta2 = input()
            if dorinta2 == "da":
                print("Scrieti numele si numarul persoanei pe care vreti sa o adaugati: ")
                nume2 = input()
                numar = int(input())
                agenda_telefonica[nume_persoana(nume2)] = numar
                print("Ati adaugat cu succes pe", nume_persoana(nume2), "in contactele noastre")
                print("Agenda ta telefonica arata acum asa", agenda_telefonica.keys())
            else:
               print("ok")
               bucla = 0
    else:
       print("Ne pare rau, dar ", nume_persoane(nume), "nu a fost gasita in contactele noastre")
       print("Incercati din nou")
elif dorinta == "nu":
    print("ok")
print("Va multumim ca ati folosit agenda calculatorului")


