import random

potions = 0
points_de_vie = 50
player_1 = player_2 = points_de_vie
attaque_player_1 = random.randint(5, 10)
attaque_player_2 = random.randint(5, 15)

print(f"Le player 1 à {player_1} de vie")
print(f"Le player 2 à {player_2} de vie")
print(f"Le player 1 à {potions} de potions")

while player_1 != 0 or player_2 != 0:
    attaque = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2)? ")
    if attaque.isdigit():
        attaque = int(attaque)
        if attaque == 1:
            player_2 = player_2 - attaque_player_1
            print(f"Le score de player 1 dans l'attaque est de {player_1}")
            player_1 = player_1 - attaque_player_2
            print(f"Le score de player 2 dans l'attaque est de {player_2}")
            print(f"Le player 1 à {potions} de potion")
        if attaque == 2:
            while potions > 0:
                potions += 1
                if potions == 0:
                    player_1 = player_1 + random.randint(15, 50)
                    player_1 = player_1 - attaque_player_2
                    print(f"le score de player un avec la potion est de {player_1}")
                    print(f"le score de player 2 qui n'a pas du changer {player_2}")
                    print(f"Le player 1 il lui reste {potions} potions")
                elif potions == 3:
                    print("Vous n'avez plus de potions")       
        if player_1 <=0 or player_2 <= 0:
            if player_1 <= 0:
                print("Vous avez perdu")
                break
            elif player_2 <= 0:
                print("Vous avez gagné")
                break
            
    


    
