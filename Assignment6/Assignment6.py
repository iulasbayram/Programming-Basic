# Student Name: Ismail Ulas Bayram
# Student ID: 220201040

import random

# Below that, I wrote function for openning file and selecting list of pokemon randomly.
def random_list():
    pokemon_list=[]
    file=open("pokedox.txt","r")
    file1=file.readlines()
    for line in file1[1:] :
        sub_pokemon_list=[]
        for a in line.split():
            try:
                int_a=int(a)
                sub_pokemon_list.append(int_a)
            except:
                sub_pokemon_list.append(a)

# Below that, after openning list, I wrope "append" and I put all of pokemon into pokemon list.
        pokemon_list.append(sub_pokemon_list)
    file.close()

# Below that, I choosed three pokemon into player pokemon list randomly.
    player_pokemon_list=[]
    for r in range(3):
        player_pokemon_list.append(random.choice(pokemon_list))
    return player_pokemon_list

# And then, I assigned function to value.
player1=random_list()
player2=random_list()

# Below that, I wrote second function for fighting mutually.
def fighting_mutually():

    # I composed random pokemon list to specify order of player.
    pokemon_random_list=[player1,player2]
    first_player=random.choice(pokemon_random_list)
    if first_player==player1:
        second_player=player2
    elif first_player==player2:
        second_player=player1
    print
    print "First player's pokemon list is " , first_player
    print
    print "Second player's pokemon list is " , second_player

    # I used for loop because I took three pokemon and my program should return three times according to count of pokemon.
    for k in range(3):
        print

        # Below that, I took raw input because of selecting pokemon that I want in pokemon list.
        player1_pokemon=raw_input("If you are first player, please enter pokemon name according to list:\n")
        player1_pokemon=player1_pokemon[:1].upper() + player1_pokemon[1:].lower()
        for i in range(len(first_player)):
            if first_player[i][0]==player1_pokemon:
                selected_pokemon1=first_player[i]

        player2_pokemon=raw_input("If you are second player, please enter pokemon name according to list:\n")
        for j in range(len(second_player)):
            if second_player[j][0]==player2_pokemon:
                selected_pokemon2=second_player[j]

        # According to weekness and type, I determined attack point of pokemons.
        if selected_pokemon1[3]==selected_pokemon2[4]:
            selected_pokemon1[2]=selected_pokemon1[2] + 10
            print selected_pokemon1[0] + " added +10 attack point"

        if selected_pokemon2[3]==selected_pokemon1[4]:
            selected_pokemon2[2]=selected_pokemon2[2] + 10
            print selected_pokemon2[0] + " added +10 attack point"

        # I wrote while loop for fighting.
        x= True
        while x:


            selected_pokemon2[1]=selected_pokemon2[1] - selected_pokemon1[2]
            print
            print selected_pokemon1[0] + " attack strike!"
            print
            if selected_pokemon2[1] <=0 :
                print selected_pokemon2[0] + " is dead"
                print
                print "First player's pokemon " , selected_pokemon1[0] , " WON !!!"

                win_or_lose(second_player)

                # Below that, I wrote two while loop to remove dead pokemon.
                count2=0
                while count2 < len(second_player):
                    if second_player[count2][0]==selected_pokemon2[0]:
                        second_player.pop(count2)
                        print
                        print "The available list of second player is " , second_player
                    count2 += 1
                x= False

            else:
                selected_pokemon1[1]= selected_pokemon2[1] - selected_pokemon2[2]
                print selected_pokemon2[0] + " attack strike!"
                print
                if selected_pokemon1[1] <=0 :
                    print selected_pokemon1[0] + " is dead"
                    print
                    print "Second player's pokemon " , selected_pokemon2[0] , " WON !!!"

                    win_or_lose(first_player)

                    count1=0
                    while count1 <len(first_player):
                        if first_player[count1][0]==selected_pokemon1[0]:
                            first_player.pop(count1)
                            print
                            print "The available list of first player is  " , first_player
                        count1 +=1
                    x= False

# Finally, I wrote function to finish game.
# If count of user's pokemons are exhaustion, this function execute and be assigned to selected parameter.
def win_or_lose(player_list):
    if player_list==[]:
        print
        print "CONGRATULATIONS!!! YOU WIN !!!!!!"
    else:
        print
        print "THE WAR DIDN'T FINISH YET.. "


fighting_mutually()