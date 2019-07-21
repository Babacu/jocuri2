import random
print("'Spanzuratoarea' cu cifre.")
print("Doriti sa jucati? ")
startTheGame = input()
loop = 1
if startTheGame == "da":
    while loop == 1:
        # The computer will choose three random numbers, each one chosen from three different lists from 0 to 9
        print('Ghiceste prima cifra:')
        attempts = 10
        firstListOfNumbers = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
        secondListOfNumbers = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
        thirdListOfNumbers = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
        firstNumber = random.choice(firstListOfNumbers)
        secondNumber = random.choice(secondListOfNumbers)
        thirdNumber = random.choice(thirdListOfNumbers)
        print(str(firstNumber), str(secondNumber), str(thirdNumber))
        print('_ ' * 3)
        guessTheFirstNumber = input()
        loop2 = 1
        loop3 = 1
        loop4 = 1
        while loop2 == 1:
            if guessTheFirstNumber == str(firstNumber):
                print(str(firstNumber) + '_ ' * 2)
                print("Ghicste a doua cifra:")
                guessTheSecondNumber = input()
                while loop3 == 1:
                    if guessTheSecondNumber == str(secondNumber):
                        print(str(firstNumber) + str(secondNumber) + '_')
                        print("Ghiceste a treia cifra: ")
                        guessTheThirdNumber = input()
                        while bucla2 == 1:
                            if guessTheThirdNumber == str(thirdNumber):
                                print(str(firstNumber)+str(secondNumber)+str(thirdNumber))
                                loop2 = 0
                                loop3 = 0
                                loop4 = 0
                            else:
                                print("Mai incearca")
                                attempts = attempts-1
                                print("Ti-au mai ramas", attempts, "vieti")
                                if attempts == 0:
                                    loop2 = 0
                                    loop3 = 0
                                    loop4 = 0
                                    print("Game over")
                                else:
                                    print("Tasteaza o cifra: ")
                                    guessTheThirdNumber = input()
                    else:
                        print("Mai incearca: ")
                        attempts = attempts-1
                        print("Ti-au mai ramas", attempts, "vieti")
                        if attempts == 0:
                            loop2 = 0
                            loop3 = 0
                            loop4 = 0
                            print("Game over")
                        else:
                            print("Tasteaza o cifra: ")
                            guessTheSecondNumber = input()
            elif guessTheFirstNumber != str(firstNumber):
                print("Mai incearca")
                attempts = attempts-1
                print("Ti-au mai ramas", attempts, "vieti")
                if attempts == 0:
                    loop2 = 0
                    loop3 = 0
                    loop4 = 0
                    print("Game over")
                else:
                    print("Tasteaza o cifra: ")
                    guessTheFirstNumber = input()
        print("Doriti sa mai jucati? ")
        playAgain = input()
        if playAgain == "nu":
            loop = 0
        else:
            continue
else:
    print("ok")
print("va multumim!")
