import random

potions = 3
points_de_vie = 50
player_1 = player_2 = points_de_vie
attaque_player_1 = random.randint(5, 10)
attaque_player_2 = random.randint(5, 15)

print(player_1)
print(player_2)
print(potions)

while player_1 or player_2 != 0:
    attaque = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2)? ")
    attaque = int(attaque)
    if attaque == 1:
        player_2 = player_2 - attaque_player_1
        print(player_1)
        player_1 = player_1 - attaque_player_2
        print(player_2)
    if attaque == 2:
        potions = random.randint(15, 50)
        player_1 = player_1 + potions
        print(player_1)
        potions = potions - 1
        player_1 = player_1 - attaque_player_2
        print(player_1)
        print(player_2)
if player_1 and player_1 <= 0:
    if player_1 == 0:
        print("Vous avez perdu")
    elif player_2 == 0:
        print("Vous avez gagné")

    
