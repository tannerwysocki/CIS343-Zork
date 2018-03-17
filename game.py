import random
import Observable
import Observer

class Player:
    attack = random.randint(10,21)
    health = random.randint(100,121)

class NPC:
    #Health stat for the NPC
    health = 0
    #Attack attribute for NPC
    attack = 0
    #Friendly attribute for NPC. 1 if friendly, 0 if enemy.
    friendly = 0

class Person(NPC):
    health = 100
    attack = 0
    friendly = 0

class Zombie(NPC):
    #TODO
    pass

class Vampire(NPC):
    #TODO
    pass

class Ghoul(NPC):
    #TODO
    pass

class Werewolf(NPC):
    #TODO
    pass

class Neighborhood(Observable):
    #TODO
    pass

class House(Observer):
    mosters = []
    monster_type = {'1':Person(),'2':Zombie(),'3':Vampire(),'4':Ghoul(),'5':
    Werewolf()}
    def __init__(self):
        monster_count = random.randint(1,11)
        for i in monster_count:
            monsters.append(monster_type[monster_count])
    def update(self):
        print("Update")
