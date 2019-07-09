import random
print("Piatra, hartie, foarfece")
print("Doriti sa jucati?")
dorinta = input()
bucla2 = 1
if dorinta == "da" or dorinta == "Da":
    while bucla2 == 1:
        scorul_jucatorului = 0
        scorul_calculatorului = 0
        bucla = 1
        while bucla == 1:
            variantele_calculatorului = ["Piatra", "Hartie", "Foarfeca"]
            alegerea_calculatorului = random.choice(variantele_calculatorului)
            print(" ")
            print("Alege o varianta: piatra/hartie/foarfeca")
            varianta = input()
            if varianta == "piatra" or varianta == "Piatra":
                if alegerea_calculatorului == "Piatra":
                    print("Calculatorul a ales tot", alegerea_calculatorului)
                    print(" ")
                    print("Scorul este: ", scorul_jucatorului, "-", scorul_calculatorului)
                elif alegerea_calculatorului == "Hartie":
                    scorul_calculatorului = scorul_calculatorului + 1
                    print("Calculatorul a ales", alegerea_calculatorului)
                    print(" ")
                    print("Scorul este: ", scorul_jucatorului, "-", scorul_calculatorului)
                    if scorul_calculatorului == 3:
                        print("Ai pierdut, incearca din nou!")
                        bucla = 0
                elif alegerea_calculatorului == "Foarfeca":
                    scorul_jucatorului = scorul_jucatorului + 1
                    print("Calculatorul a ales", alegerea_calculatorului)
                    print(" ")
                    print("Scorul este: ", scorul_jucatorului, "-", scorul_calculatorului)
                    if scorul_jucatorului == 3:
                        print("Felicitari, ai castigat")
                        bucla = 0
            if varianta == "hartie" or varianta == "Hartie":
                if alegerea_calculatorului == "Hartie":
                    print("Calculatorul a ales tot", alegerea_calculatorului)
                    print(" ")
                    print("Scorul este: ", scorul_jucatorului, "-", scorul_calculatorului)
                elif alegerea_calculatorului == "Foarfeca":
                    scorul_calculatorului = scorul_calculatorului + 1
                    print("Calculatorul a ales", alegerea_calculatorului)
                    print(" ")
                    print("Scorul este: ", scorul_jucatorului, "-", scorul_calculatorului)
                    if scorul_calculatorului == 3:
                        print("Ai pierdut, incearca din nou!")
                        bucla = 0
                elif alegerea_calculatorului == "Piatra":
                    scorul_jucatorului = scorul_jucatorului + 1
                    print("Calculatorul a ales", alegerea_calculatorului)
                    print(" ")
                    print("Scorul este: ", scorul_jucatorului, "-", scorul_calculatorului)
                    if scorul_jucatorului == 3:
                        print("Felicitari, ai castigat")
                        bucla = 0
            if varianta == "Foarfeca" or varianta == "foarfeca":
                if alegerea_calculatorului == "Foarfeca":
                    print("Calculatorul a ales tot", alegerea_calculatorului)
                    print(" ")
                    print("Scorul este: ", scorul_jucatorului, "-", scorul_calculatorului)
                elif alegerea_calculatorului == "Piatra":
                    scorul_calculatorului = scorul_calculatorului + 1
                    print("Calculatorul a ales", alegerea_calculatorului)
                    print(" ")
                    print("Scorul este: ", scorul_jucatorului, "-", scorul_calculatorului)
                    if scorul_calculatorului == 3:
                        print("Ai pierdut, incearca din nou!")
                        bucla = 0
                elif alegerea_calculatorului == "Hartie":
                    scorul_jucatorului = scorul_jucatorului + 1
                    print("Calculatorul a ales", alegerea_calculatorului)
                    print(" ")
                    print("Scorul este: ", scorul_jucatorului, "-", scorul_calculatorului)
                    if scorul_jucatorului == 3:
                        print("Felicitari, ai castigat")
                        bucla = 0
        print("Doriti sa mai jucati?")
        dorinta2 = input()
        if dorinta2 == "da" or dorinta2 == "Da":
            continue
        else:
            print("Va multumim ca ati ales sa va jucati!")
            bucla2 = 0
else:
    print("ok")
    print("Va multumim!")
