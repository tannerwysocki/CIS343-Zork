import random
from Observable import Observable
from Observer import Observer

class Player:
    __inventory = {}
    __attack = random.randint(10,20)
    __health = random.randint(100,120)

class NPC:
    #Health stat for the NPC
    __health = 0
    #Attack attribute for NPC
    __attack = 0
    #Friendly attribute for NPC. 1 if friendly, 0 if enemy.
    __friendly = 0

class Person(NPC):
    def __init__(self):
        self.__health = 100
        self.__attack = 0
        self.__friendly = 1

class Zombie(NPC):
    def __init__(self):
        self.__health = random.randint(50,100)
        self.__attack = random.randint(0,10)
        self.__friendly = 0

class Vampire(NPC):
    def __init__(self):
        self.__health = random.randint(100,200)
        self.__attack = random.randint(10,20)
        self.__friendly = 0

class Ghoul(NPC):
    def __init__(self):
        self.__health = random.randint(40,80)
        self.__attack = random.randint(15,30)
        self.__friendly = 0

class Werewolf(NPC):
    def __init__(self):
        self.health = 200
        self.attack = random.randint(15,30)
        self.friendly = 0

class Neighborhood(Observable):
    __grid = [[],[],[]]
    __monster_count = 0
    def __init__(self):
        for i in range(0,4):
            self.grid[0].append(House())
            self.grid[1].append(None)
            self.grid[2].append(House())
    def set_monster_count(count):
        __monster_count = count
    def get_monster_count():
        return __monster_count

class Weapon():
    __name = ''
    __attack = 0.0

class House(Observer):
    monsters = []
    monster_type = {1:Person(), 2:Zombie(), 3:Vampire(), 4:Ghoul(), 5:Werewolf()}
    def __init__(self):
        monster_count = random.randint(1,10)
        print(monster_count)
        for i in range(0,monster_count):
            self.monsters.append(self.monster_type[random.randint(2,5)])
            monster_count++
    def update(self,neighborhood):
        neighborhood.set_monster_count(neighborhood.get_monster_count-1)

def main():
    test = Neighborhood()

main()
