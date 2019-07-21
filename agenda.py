def personsName(name):
    return  name

loop = 1
print("Buna ziua")
sayHello = input()
#You are welcome to the computer directory
print("Bine ati venit in agenda telefonica calculatorului")
phoneContacts = {"Sebi" : 770421464, "Balau" : 748113188, "Bianca" : 768152514,
                     "Crisan" : 724248152}
print("Doriti sa accesati contactele noastre")
#want to get in the directory
GetInTheDirectory = input()
if GetInTheDirectory == "da":
    print("Contactele noastre sunt: ", phoneContacts.keys())
    print("Pe cine doriti sa cautati in agenda?")
    #Insert the person's name you want to seach
    name = input()
    if personsName(name) in phoneContacts:
        print("Numarul sau este", phoneContacts[personsName(name)])
        while loop == 1:
            print("Vreti sa adaugati contacte noi in agenda? ")
            # Add new people in the directory
            add = input()
            if add == "da":
                print("Scrieti numele si numarul persoanei pe care vreti sa o adaugati: ")
                nameOfTheNewPerson = input()
                phoneNumber = int(input())
                phoneContacts[personsName(nameOfThePerson)] = phoneNumber
                print("Ati adaugat cu succes pe", personsName(nameOfTheNewPerson), "in contactele noastre")
                print("Agenda ta telefonica arata acum asa", phoneContacts.keys())
            else:
               print("ok")
               loop = 0
    else:
       print("Ne pare rau, dar ", personsName(name), "nu a fost gasita in contactele noastre")
       print("Incercati din nou")
elif GetInTheDirectory == "nu":
    print("ok")
print("Va multumim ca ati folosit agenda calculatorului")
