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
        if(action.upper() == 'C'):
            catch(self)
        elif(action.upper() == 'S'):
            shop(self)
        elif(action.upper() == 'B'):
            battle(self)
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

    for item in shop:
        print(f"{item.name}: {item.cost}")

    print("What would you like to buy?")
    # take in player input
    # check for enough money
    # if they have enough money, give them the items.

def battle(player):
    # start a battle between the player and an enemy trainer
        # 1. start by generating a random enemy trainer
        # 2. make a variable called battling and set it equal to True
        # 3. make a while loop using the battling variable
            # every turn in the battle is one run through the loop

    # do the following every turn in battle:
        # 1. print name of enemy trainer
        # 2. print name of enemy trainer's current pokemon
        # 3. print enemy trainer's pokemon's current hp 
        # 4. print name of your current pokemon
        # 5. print HP of your current pokemon
        # 6. print your current pokemon's moves
        # 7. print the actions the player can take 
        #   1. use a move
        #   2. swap pokemon
        #   3. punch enemy trainer
        # 8. ask player to make a choice just like in the act() method
        # 9. use an if statement to run the right code based on their choice
            # either use a move, swap pokemon, punch enemy.
    pass

def view_pokemon(player):
    if player.pokemon: # checks to see if list is empty or not
        for pokemon in player.pokemon:
            print(f"\nName: {pokemon.name}, Level: {pokemon.LVL}, Type: {pokemon.type}, Weakness: {pokemon.weakness}")
            for move in pokemon.moves:
                print(f"Move: {move.name}, Power: {move.power}, Type: {move.type}")

def eliteFour(player):
    # fight the elite four
    pass

def game():
    name = input("Welcome to the world of Pokemon! What is your name?\n")
    gender = input("Are you a boy (M) or a girl (F) or nonbinary (X) \n")

    player1 = Player(name, gender)

    while player1.level <= 25:
        player1.act()

    print("You have passed Level 25. It's time to fight the Elite 4!")
    eliteFour()

game()