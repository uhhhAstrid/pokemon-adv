import random

class EnemyTrainer:
    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon = pokemon
        self.money = random.randint(1,99999)

class Pokemon:
    def __init__(self, type, name, moves, weakness):
        self.type = type
        self.name = name
        self.moves = moves
        self.weakness = weakness
        self.fainted = False
        self.LVL = random.randint(1,99)
        self.HP = random.randint(1,999) + self.LVL
        self.DEF = random.randint(1,200) + self.LVL
        self.ATK = random.randint(1,200) + self.LVL      

class Move:
    def __init__(self, type, name, power):
        self.type = type
        self.name = name
        self.power = power

def loadNameList():
    with open("names.txt", "r") as name_file:
        names = name_file.read().splitlines()
    return names

def loadPokemonList():
    with open("pokemon.txt", "r") as pokemon_file:
        pokemon_list = pokemon_file.read().splitlines()
    return pokemon_list

def loadMoveList():
    with open("moves.txt", "r") as move_file:
        move_list = move_file.read().splitlines()
    return move_list

def loadTypeList():
    with open("types.txt", "r") as type_file:
        type_list = type_file.read().splitlines()
    return type_list

def generateType():
    type = random.choice(loadTypeList())
    return type

def generateMove():
    # create the move's info
    name = random.choice(loadMoveList())
    type = generateType()
    power = random.randint(1,200)

    # make the move
    move = Move(type, name, power)
    return move

def generatePokemon():
    # create the pokemon's info
    type = generateType()
    name = random.choice(loadPokemonList())
    moves = []
    for i in range (4):
        move = generateMove()
        moves.append(move)
    weakness = generateType()
    
    # make the pokemon
    pokemon = Pokemon(type, name, moves, weakness)
    return pokemon

def generateEnemyTrainer():
    # create the trainer's info
    name = random.choice(loadNameList())
    pokemon = generatePokemon()
    
    # make the trainer
    trainer = EnemyTrainer(name, pokemon)
    return trainer