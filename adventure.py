import random
import pokemon
import time

class Player():
    def __init__(self, name, gender):
        self.level = 1
        self.money = 0
        self.name = name
        self.gender = gender
        self.attack = 0
        self.defense = 0
        self.pokemon = []
        self.items = [] 
    
    def act(self):
        action = input("'C' to try and catch a pokemon, 'S' to visit shop, 'B' to battle, 'P' to see caught pokemon, or 'Q' to quit. \n")
        action = action.strip()
        action = action.upper()

        if(self.level > 2):
            print("You're ready. It's time.")
            eliteFour(self)

        if(action.upper() == 'C'):
            catch(self)
        elif(action.upper() == 'S'):
            shop(self)
        elif(action.upper() == 'B'):
            enemy_trainer = pokemon.generateEnemyTrainer()
            battle(self, enemy_trainer)
            self.act()
        elif(action.upper() == 'P'):
            view_pokemon(self)
        elif(action.upper() == 'Q'):
            print("Thanks for playing! Goodbye for now!")
            quit()
        else:
            print("I'm sorry, I didn't recognize that command.")

def catch(player):
    # generate a random pokemon
    random_pokemon = pokemon.generatePokemon()

    # print out the name of the pokemon
    print(random_pokemon.name)

    # print out the level of the pokemon
    print(f"{random_pokemon.LVL}")

    # allow player to choose one of the following:
        # 1. throw a pokeball 
        # 2. find a different pokemon
        # 3. stop catching pokemon
    action = input("What would you like to do? Try to catch (C), find a different pokemon (P), or stop catching (X)")
    action = action.strip()
    action = action.upper()
    if(action == 'C'):
        numberToBeat = 50
        catchChance = random.randint(0,100) + player.level

        if catchChance > numberToBeat:
            print(f"You caught a {random_pokemon.name}!!!!! It's level {random_pokemon.LVL}!")
            player.pokemon.append(random_pokemon)
            player.level = player.level + 1
        else:
            print(f"You failed to catch the {random_pokemon.name}. It ran away!")
        catch(player)
    elif(action == 'P'):
        catch(player)
    elif(action == 'X'):
        player.act()

def shop(player):
    print("Hi there! Welcome to my shop!!")
    time.sleep(1)
    print("~~~ ✨🎵shop music🎵✨ ~~~")
    time.sleep(1)
    print("PLEASE buy something PLEASEEEEEEEE 😭😭😭🥺🥺🥺!!!👉👈!!\n\n")
    time.sleep(3)
    print("~~~ after an awkward pause, the shopkeeper is drowned out by ✨🎵soothing shop music🎵✨ ~~~")
    
    # make the items (I'll clean this up later)
    potion = pokemon.Item("potion", 10)
    pokeball = pokemon.Item("pokeball", 5)
    tastySandwich = pokemon.Item("A tasty sandwich. 🥪. Yum!", 999)
    
    # make the shop
    shop = pokemon.Shop()
    
    # stock the shop with the item
    shop.items.append(potion)
    shop.items.append(pokeball)
    shop.items.append(tastySandwich)

    for item in shop.items:
        print(f"{item.name}: {item.cost}")

    print("What would you like to buy?")
    # take in player input
    # check for enough money
    # if they have enough money, give them the items.

def battle(player, enemy_trainer):
    battling = True
    win = False
    
    # choose a pokemon to send out first
    view_pokemon(player)
    poke_choice = int(input("Which pokemon would you like to have out for this battle? enter the pokemon's ID [0-30]"))
    chosen_pokemon = player.pokemon[poke_choice]
    
    enemyHP = enemy_trainer.pokemon.HP 

    # ask the player what they are doing on their turn
    while(battling):
        
        action = input("Use a move for your pokemon (M), Swap Pokemon (S), Punch enemy trainer (P), Run away (R)")
        action = action.upper()
        action = action.strip()

        # choose a pokemon move
        if action == "M":
    
                # print out moves
                move_number = 0
                for move in chosen_pokemon.moves:
                    print(move.name, move.power, str(move_number))
                    move_number = move_number + 1
                
                # ask player to pick one
                used_move_id = int(input("Which move? 0, 1, 2, or 3?"))
                used_move = chosen_pokemon.moves[used_move_id]

                # attack with move ((enemy pokemon health - pokemon attack + pokemon move power * 2 (if weak))
                if(used_move.type == enemy_trainer.pokemon.weakness):
                    enemyHP -= 2*(chosen_pokemon.ATK + used_move.power)
                else:
                    enemyHP -= (chosen_pokemon.ATK + used_move.power)
                
                if(enemyHP <= 0):
                    battling = False
                    win = True
                
                print(str(enemyHP))
        
        # switch pokemon
        elif action == "S":
            # 1. ask which pokemon to switch to
            view_pokemon(player)

            # 2. select that pokemon
            poke_choice = int(input("Which pokemon would you like to have out for this battle? enter the pokemon's ID [0-30]"))

            # 3. change pokemon
            chosen_pokemon = player.pokemon[poke_choice]

        # punch enemy trainer
        elif action == "P":

            # 1. enemy trainer health - player attack
            enemy_trainer.HP -= player.attack

            # 2. if enemy trainer health at 0, end battle
            if(enemy_trainer.HP <= 0):
                battling = False
                win = True
        
        # run away
        elif action =="R":
            battling = False
            win = False
    
        # after all that has been checked, enemy turn:
        enemy_move_id = random.randint(0,3)
        enemy_move = enemy_trainer.pokemon.moves[enemy_move_id]
        print(f"{enemy_trainer.name}'s {enemy_trainer.pokemon.name} uses {enemy_move.name}!!!")
        if(enemy_move.type == chosen_pokemon.weakness):
            damage = 2*(enemy_trainer.pokemon.ATK + enemy_move.power)
            chosen_pokemon.HP -= damage
            print(f"The move did {damage} damage!!!!!!!!!!!")
        else:
            damage = (enemy_trainer.pokemon.ATK + enemy_move.power)
            chosen_pokemon.HP -= damage
            print(f"The move did {damage} damage!!!!!!!!!!!")
        if(chosen_pokemon.HP <= 0):
            battling = False
            win = False

    if(win):
        print(f"You win! Congratulations! You got ${enemy_trainer.money}")
    else:
        amount_lost = int(0.2*(player.money))
        player.money -= amount_lost
        print(f"You lost! Sorry :(. You lost {amount_lost}")  


def view_pokemon(player):
    if player.pokemon: # checks to see if list is empty or not
        poke_ID = 0
        for pokemon in player.pokemon:
            print(f"\nName: {pokemon.name}, Level: {pokemon.LVL}, Type: {pokemon.type}, Weakness: {pokemon.weakness}, ID: {poke_ID}")
            poke_ID = poke_ID + 1
            for move in pokemon.moves:
                print(f"Move: {move.name}, Power: {move.power}, Type: {move.type}")

def eliteFour(player):

    # generate the 4 champions of the elite 4

    # generate champion: blue
    ala_move_1 = pokemon.Move("Psychic", "Warp Reality", 200)
    ala_move_2 = pokemon.Move("Psychic", "Reverse Gravity", 200)
    ala_move_3 = pokemon.Move("Psychic", "Bend Spoon", 2)
    ala_move_4 = pokemon.Move("Psychic", "Soup Teleportation", 20)
    ala_moves = [ala_move_1, ala_move_2, ala_move_3, ala_move_4]
    alakazam = pokemon.Pokemon("Psychic", "Alakazam", ala_moves, "Dark")
    alakazam.LVL = 80
    alakazam.ATK = 450
    alakazam.DEF = 450
    alakazam.HP = 4500
    blue = pokemon.EnemyTrainer("Blue", alakazam)
    
    # generate red
    pika_move_1 = pokemon.Move("Electric", "Thunderbolt", 200)
    pika_move_2 = pokemon.Move("Electric", "Super Pikachu Slam", 200)
    pika_move_3 = pokemon.Move("Electric", "Thunder Explosion", 200)
    pika_move_4 = pokemon.Move("Electric", "Thunder Punch", 200)
    pika_moves = [pika_move_1, pika_move_2, pika_move_3, pika_move_4]
    pikachu = pokemon.Pokemon("Electric", "Pikachu", pika_moves, "Ground")
    pikachu.LVL = 99
    pikachu.ATK = 678
    pikachu.DEF = 500
    pikachu.HP = 7777
    red = pokemon.EnemyTrainer("Red", pikachu)
    
    # generate leon
    mega_move_1 = pokemon.Move("Fire", "Mega Fire Blast", 333)
    mega_move_2 = pokemon.Move("Flying", "Arial Finale", 333)
    mega_move_3 = pokemon.Move("Rock", "The Rock of Gibraltar", 333)
    mega_move_4 = pokemon.Move("Dragon", "Mega Dragon Death Beam", 333)
    mega_moves = [mega_move_1, mega_move_2, mega_move_3, mega_move_4]
    MegaCharizardX = pokemon.Pokemon("Fire", "Mega Charizard X", mega_moves, "Water")
    MegaCharizardX.LVL = 100
    MegaCharizardX.ATK = 999
    MegaCharizardX.DEF = 999
    MegaCharizardX.HP = 9999
    Leon = pokemon.EnemyTrainer("Leon", MegaCharizardX)
    
    # generate cynthia
    giga_move_1 = pokemon.Move("Normal", "Giga Impact", 999)
    giga_move_2 = pokemon.Move("Dragon", "Draco Meteor Shower", 1111)
    giga_move_3 = pokemon.Move("Dragon", "Giga Dragon: Final Form: Rush of the Thousand Angry Dragons", 9999)
    giga_move_4 = pokemon.Move("Fighting", "Worldbreaker", 2222)
    giga_moves = [giga_move_1, giga_move_2, giga_move_3, giga_move_4]
    GigaGarchomp = pokemon.Pokemon("Dragon", "Giga Garchomp", giga_moves, "Fairy")
    Cynthia = pokemon.EnemyTrainer("Cynthia", GigaGarchomp)

    # fight the elite four
    print("Fight against Pokemon Champion: Blue!")
    battle(player, blue) # Alakazam
    
    print("Fight against Pokemon Champion: Red!")
    battle(player, red) # Pikachu

    
    print("Fight against Pokemon Champion: Leon!")
    battle(player, Leon) # Mega Charizard X

    
    print("Fight against Final Pokemon Champion: Cynthia!!!!")
    battle(player, Cynthia) # GigaGarchomp

    print("CONGRATULATIONS!!!! YOU HAVE DEFEATED THE ELITE FOUR!!!!! >:DDD!!! YOU WIN!!!!!!")

def game():
    name = input("Welcome to the world of Pokemon! What is your name?\n")
    gender = input("Are you a boy (M) or a girl (F) or nonbinary (X) \n")

    player1 = Player(name, gender)

    while player1.level <= 2:
        player1.act()

    print("You have passed Level 25. It's time to fight the Elite 4!")
    eliteFour()

game()