import random
import time
# the blacjack game with 2 players
#There are the ace, qween, king and jack's values
A = 11
J = 2
Q = 3
K = 4
#I'll create a list with all the cards
deckOfCards = [A, J, Q, K, 7, 8, 9, 10]*4
# I create a list where will be typed the cards of the players
firstPlayersHand = []
secondPlayersHand = []
#Welcoming to the game
print("Welcome to blackjack game with two players!")
#Greeting
print("First player's name: ")
firstPlayersName = input()
print("Second player's name: ")
secondPlayersName = input()
# I have to create a loop to repeat the movements of the first player
loop = 1
#The computer will ask you if you want to play
print("Do you want to play?")
#Answer the question
answer = input()   
if answer == "Yes" or "yes":
    #The deck has to be shuffled
    random.shuffle(deckOfCards)
    #Now the first player will extract two cards from the shuffled deck, check them and sum their values
    print("There is ", firstPlayersName, "'s hand")
    #I want to make a pause between the actions
    time.sleep(1)
    firstPlayersHand = deckOfCards[0:2]
    #the first two cards are deleted from the list because they were distributed
    del deckOfCards[0:2]
    print(firstPlayersHand)
    sumOfFirstPlayersCards = firstPlayersHand[0] + firstPlayersHand[1]
    print("Their sum is: ", sumOfFirstPlayersCards)
    time.sleep(1)
    #The sum of the cards has to be more or equal to 15 if you want to stop
    while loop == 1:
        if sumOfFirstPlayersCards < 15:
            #The player must get another card to have at least 15 in the hand
            print("You need to have at least 15 to stop")
            time.sleep(1)
            print("Press any key to get another card ")
            input()
            # Here's where the first player gets another card
            firstPlayersHand.append(deckOfCards[0])
            print(firstPlayersHand)
            #Now the computer will sum again the cards to verify if it's more than 15
            sumOfFirstPlayersCards = sumOfFirstPlayersCards + deckOfCards[0]
            del deckOfCards[0]
            print("Their sum is: ", sumOfFirstPlayersCards)
        elif sumOfFirstPlayersCards >= 15 and sumOfFirstPlayersCards < 21:
            #Now the player can decide if he wants to stop or not
            print("Do you want more? ")
            #If he wants more he will type yes
            answer2 = input()
            if answer2 == "yes" or answer2 =="Yes":
                #the player takes another card
                firstPlayersHand.append(deckOfCards[0])
                print(firstPlayersHand)
                time.sleep(1)
                sumOfFirstPlayersCards = sumOfFirstPlayersCards + deckOfCards[0]
                del deckOfCards[0]
                print("Their sum is: ", sumOfFirstPlayersCards)
            else:
                #He doesn't want any card
                print("it's suficient for", firstPlayersName)
                break
        #the player wins when he has more than the other player or when he has 21
        elif sumOfFirstPlayersCards == 21:
            print(firstPlayersName, "won!")
            break
        #and he loses when he has fewer than the other player or more than 21
        elif sumOfFirstPlayersCards > 21:
            print(firstPlayersName, "lost!")
            break
    #now, we will do the same but with the second player
    print("There is ", secondPlayersName, "'s hand")
    time.sleep(1)
    secondPlayersHand = deckOfCards[0:2]
    del deckOfCards[0:2]
    print(secondPlayersHand)
    sumOfSecondPlayersCards = secondPlayersHand[0] + secondPlayersHand[1]
    print("Their sum is: ", sumOfsecondPlayersCards)
    time.sleep(1)
    loop2 = 1
    while loop2 == 1:
        if sumOfSecondPlayersCards < 15:
            print("You need to have at least 15 to stop")
            time.sleep(1)
            print("Press any key to get another card ")
            input()
            secondPlayersHand.append(deckOfCards[0])
            print(secondPlayersHand)
            sumOfSecondPlayersCards = sumOfSecondPlayersCards + deckOfCards[0]
            del deckOfCards[0]
            print("Their sum is: ", sumOfSecondPlayersCards)
        elif sumOfSecondPlayersCards >= 15 and sumOfSecondPlayersCards < 21:
            print("Do you want more? ")
            answer3 = input()
            if answer3 == "yes" or answer3 =="Yes":
                secondPlayersHand.append(deckOfCards[0])
                print(secondPlayersHand)
                time.sleep(1)
                sumOfSecondPlayersCards = sumOfSecondPlayersCards + deckOfCards[0]
                del deckOfCards[0]
                print("Their sum is: ", sumOfSecondPlayersCards)
            else:
                print("it's suficient for", secondPlayersName)
                break
        elif sumOfSecondPlayersCards == 21:
            print(secondPlayersName, "won!")
            break
        elif sumOfSecondPlayersCards > 21:
            print(secondPlayersName, "lost!")
            break
print("Thank you!")
#I have to declare functions
                
                        
