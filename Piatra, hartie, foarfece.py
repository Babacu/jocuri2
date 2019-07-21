import random
def results(oneOfPCOptions, playersResult, PCsResult):
    print("Calculatorul a ales", oneOfPCOptions)
    print(" ")
    print("Scorul este: ", playersResult, "-", PCsResult)
print("Piatra, hartie, foarfece")
print("Doriti sa jucati?")
wish = input()
loop = 1
if wish == "da" or wish == "Da":
    while loop == 1:
        playersScore = 0
        PCsScore = 0
        loop2 = 1
        while loop2 == 1:
            PCOptions = ["Piatra", "Hartie", "Foarfeca"]
            PCsChoice = random.choice(PCOptions)
            print(" ")
            print("Alege o varianta: piatra/hartie/foarfeca")
            option = input()
            if option == PCOptions[0]:
                if PCsChoice == PCOptions[0]:
                    results(PCsChoice, playersScore, PCsScore)
                elif PCsChoice == PCOptions[1]:
                    PCsScore = PCsScore + 1
                    results(PCsChoice, playersScore, PCsScore)
                elif PCsChoice == PCOptions[2]:
                    playersScore = playersScore + 1
                    results(PCsChoice, playersScore, PCsScore)
                if PCsScore == 3:
                    print("Ai pierdut, incearca din nou!")
                    loop2 = 0
                elif playersScore == 3:
                    print("Felicitari, ai castigat")
                    loop2 = 0
            if option == PCOptions[1]:
                if PCsChoice == PCOptions[1]:
                    results(PCsChoice, playersScore, PCsScore)
                elif PCsChoice == PCOptions[2]:
                    PCsScore = PCsScore + 1
                    results(PCsChoice, playersScore, PCsScore)
                elif PCsChoice == PCOptions[0]:
                    playersScore = playersScore + 1
                    results(PCsChoice, playersScore, PCsScore)
                if PCsScore == 3:
                    print("Ai pierdut, incearca din nou!")
                    loop2 = 0
                elif playersScore == 3:
                    print("Felicitari, ai castigat")
                    loop2 = 0
            if option == PCOptions[2]:
                if PCsChoice == PCOptions[2]:
                    results(PCsChoice, playersScore, PCsScore)
                elif PCsChoice == PCOptions[0]:
                    PCsScore = PCsScore + 1
                    results(PCsChoice, playersScore, PCsScore)
                elif PCsChoice == PCOptions[1]:
                    playersScore = playersScore + 1
                    results(PCsChoice, playersScore, PCsScore)
                if PCsScore == 3:
                    print("Ai pierdut, incearca din nou!")
                    loop2 = 0
                elif playersScore == 3:
                    print("Felicitari, ai castigat")
                    loop2 = 0
        print("Doriti sa mai jucati?")
        wish2 = input()
        if wish2 == "da" or wish2 == "Da":
            continue
        else:
            print("Va multumim ca ati ales sa va jucati!")
            loop = 0
else:
    print("ok")
    print("Va multumim!")
