import random
def rezultate(a, b, c):
    print("Calculatorul a ales", a)
    print(" ")
    print("Scorul este: ", b, "-", c)
print("Piatra, hartie, foarfece")
print("Doriti sa jucati?")
wish = input()
loop = 1
if wish == "da" or wish == "Da":
    while loop == 1:
        player_score = 0
        PC_score = 0
        loop2 = 1
        while loop2 == 1:
            PC_variants = ["Piatra", "Hartie", "Foarfeca"]
            PC_choice = random.choice(PC_variants)
            print(" ")
            print("Alege o varianta: piatra/hartie/foarfeca")
            option = input()
            if option == PC_variants[0]:
                if PC_choice == PC_variants[0]:
                    rezultate(PC_choice, player_score, PC_score)
                elif PC_choice == PC_variants[1]:
                    PC_score = PC_score + 1
                    rezultate(PC_choice, player_score, PC_score)
                elif PC_choice == PC_variants[2]:
                    player_score = player_score + 1
                    rezultate(PC_choice, player_score, PC_score)
                if PC_score == 3:
                    print("Ai pierdut, incearca din nou!")
                    loop2 = 0
                elif player_score == 3:
                    print("Felicitari, ai castigat")
                    loop2 = 0
            if option == PC_variants[1]:
                if PC_choice == PC_variants[1]:
                    rezultate(PC_choice, player_score, PC_score)
                elif PC_choice == PC_variants[2]:
                    PC_score = PC_score + 1
                    rezultate(PC_choice, player_score, PC_score)
                elif PC_choice == PC_variants[0]:
                    player_score = player_score + 1
                    rezultate(PC_choice, player_score, PC_score)
                if PC_score == 3:
                    print("Ai pierdut, incearca din nou!")
                    loop2 = 0
                elif player_score == 3:
                    print("Felicitari, ai castigat")
                    loop2 = 0
            if option == PC_variants[2]:
                if PC_choice == PC_variants[2]:
                    rezultate(PC_choice, player_score, PC_score)
                elif PC_choice == PC_variants[0]:
                    PC_score = PC_score + 1
                    rezultate(PC_choice, player_score, PC_score)
                elif PC_choice == PC_variants[1]:
                    player_score = player_score + 1
                    rezultate(PC_choice, player_score, PC_score)
                if PC_score == 3:
                    print("Ai pierdut, incearca din nou!")
                    loop2 = 0
                elif player_score == 3:
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
