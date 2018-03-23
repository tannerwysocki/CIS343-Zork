#!/usr/bin/env python3
import random
import sys
import time
from Observable import Observable
from Observer import Observer

# A text based adventure game.
#
#  @author Tanner Wysocki

#Non-playable character class. Can either be allies or enemies
class NPC:

    def __init__(self):
        '''
        : Initializer method for the NPC class
        '''
        #Health stat for the NPC
        self.__health = 0
        #Attack attribute for NPC
        self.__attack = 0
        #Friendly attribute for NPC. 1 if friendly, 0 if enemy.
        self.__friendly = 0
        #Name attribute for NPC
        self.name = 'NPC'

    def get_health(self):
        return self.__health

    def set_health(self,health):
        self.__health = health

    def get_name(self):
        return self.__name

#Friendly NPC class
class Person(NPC):


    def __init__(self):
        self.name = 'Person'
        self.__health = 100
        self.__attack = 0
        self.__friendly = 1

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def item_drop(self,player):
        '''
        : Determines the item dropped when the enemy is defeated
        : @param player The current player to add to the item inventory
        '''
        item = random.random()
        if(item > 0.0 and item < .055):
            print("You've picked up a Nerd Bomb!")
            player.get_weapon(4).add_inv()
        elif(item > 0.055 and item < 0.355):
            print("You've picked up a Sour Straw!")
            player.get_weapon(2).add_inv()
        elif(item > 0.355 and item < 0.600):
            print("You've picked up a Chocolate Bar!")
            player.get_weapon(3).add_inv()
        else:
            print("You've gained 3 health")
            player.set_health(player.get_health()+3)


class Zombie(NPC):

    def __init__(self):
        self.__name = 'Zombie'
        self.__health = random.randint(50,100)
        self.__attack = random.randint(0,10)
        self.__friendly = 0

    def get_attack(self):
        return random.randint(0,10)

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def set_health(self,health):
        self.__health = health

    def default_health(self):
        self.__health = random.randint(50,100)

    def item_drop(self,player):
        item = random.random()
        if(item > 0.0 and item < .055):
            print("You've picked up a Nerd Bomb!")
            player.get_weapon(4).add_inv()
        elif(item > 0.055 and item < 0.355):
            print("You've picked up a Sour Straw!")
            player.get_weapon(2).add_inv()
        elif(item > 0.355 and item < 0.600):
            print("You've picked up a Chocolate Bar!")
            player.get_weapon(3).add_inv()
        else:
            print("You've gained 3 health")
            player.set_health(player.get_health()+3)

#Vampire NPC
class Vampire(NPC):

    def __init__(self):
        self.__name = 'Vampire'
        self.__health = random.randint(100,200)
        self.__attack = random.randint(10,20)
        self.__friendly = 0

    def get_attack(self):
        return random.randint(10,20)

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def set_health(self,health):
        self.__health = health

    def default_health(self):
        self.__health = random.randint(50,100)

    def item_drop(self,player):
        item = random.random()
        if(item > 0.0 and item < .055):
            print("You've picked up a Nerd Bomb!")
            player.get_weapon(4).add_inv()
        elif(item > 0.055 and item < 0.355):
            print("You've picked up a Sour Straw!")
            player.get_weapon(2).add_inv()
        elif(item > 0.355 and item < 0.600):
            print("You've picked up a Chocolate Bar!")
            player.get_weapon(3).add_inv()
        else:
            print("You've gained 3 health")
            player.set_health(player.get_health()+3)

#Ghoul NPC
class Ghoul(NPC):

    def __init__(self):
        self.__name = 'Ghoul'
        self.__health = random.randint(40,80)
        self.__attack = random.randint(15,30)
        self.__friendly = 0

    def get_attack(self):
        return random.randint(15,30)

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def set_health(self,health):
        self.__health = health

    def default_health(self):
        self.__health = random.randint(50,100)

    def item_drop(self,player):
        item = random.random()
        if(item > 0.0 and item < .055):
            print("You've picked up a Nerd Bomb!")
            player.get_weapon(4).add_inv()
        elif(item > 0.055 and item < 0.355):
            print("You've picked up a Sour Straw!")
            player.get_weapon(2).add_inv()
        elif(item > 0.355 and item < 0.600):
            print("You've picked up a Chocolate Bar!")
            player.get_weapon(3).add_inv()
        else:
            print("You've gained 3 health")
            player.set_health(player.get_health()+3)

# Werewolf NPC
class Werewolf(NPC):

    def __init__(self):
        self.__name = 'Werewolf'
        self.__health = 200
        self.__attack = random.randint(0,40)
        self.__friendly = 0

    def get_attack(self):
        return random.randint(0,40)

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def set_health(self,health):
        self.__health = health

    def default_health(self):
        self.__health = random.randint(50,100)

    def item_drop(self,player):
        item = random.random()
        if(item > 0.0 and item < .055):
            print("You've picked up a Nerd Bomb!")
            player.get_weapon(4).add_inv()
        elif(item > 0.055 and item < 0.355):
            print("You've picked up a Sour Straw!")
            player.get_weapon(2).add_inv()
        elif(item > 0.355 and item < 0.600):
            print("You've picked up a Chocolate Bar!")
            player.get_weapon(3).add_inv()
        else:
            print("You've gained 3 health")
            player.set_health(player.get_health()+3)


# The neighborhood class is the container for the game.
# It holds a grid of houses which the player traverses
# to fight enemies. This is observed by the House class.
class Neighborhood(Observable):

    #The game world. Contains the houses of the neighborhood
    grid = [[],[]]
    #Current enemy count
    __monster_count = 0
    #Holds the observer objects, which are houses.
    __observers = []

    def __init__(self):
        '''
        : Initializer method for the Neighborhood class
        '''
        #Adds the houses to the neighborhood, creating a 2x4 grid
        for i in range(0,4):
            self.grid[0].append(House())
            self.__monster_count = self.__monster_count + self.grid[0][i].get_monster_count()
            Neighborhood.add_observer(self, self.grid[0][i])
            self.grid[1].append(House())
            self.__monster_count = self.__monster_count + self.grid[1][i].get_monster_count()
            Neighborhood.add_observer(self, self.grid[1][i])

    def set_monster_count(self, count):
        self.__monster_count = count

    def get_monster_count(self):
        return self.__monster_count

    def get_current_house(self,x,y):
        return self.grid[x][y]

    def add_observer(self, observer):
            if not observer in self.__observers:
                    self.__observers.append(observer)

    def remove_observe(self, observer):
            if observer in self.__observers:
                    self.__observers.remove(observer)

    def remove_all_observers(self):
            self.__observers = []

    def update(self):
            for observer in self.__observers:
                    observer.update()


# The base weapon class
class Weapon():

    # Holds the name of the weapon
    __name = ''
    # The weapon attack stat
    __attack = 0.0
    # The current amount of the weapon in inventory
    __stock = 0
    # The maximum allowed stock
    __max = sys.maxsize

    def attack(self):
        '''
        : Attack method for the weapon
        : Decrements the stock amount and
        : returns the attack stat for the weapon
        '''
        self.__stock = self.__stock - 1
        if(self.__stock < 0):
            self.__stock = 0
            return 0
        return self.__attack

    def add_inv(self):
        '''
        : Adds the weapon to the inventory
        : unless the amount exceeds the allowed
        : amount of items to be carried.
        '''
        if(self.__stock + 1 > self.__max):
            print("Cannot carry any more!")
        else:
           self.__stock = self.__stock + 1
    def get_name(self):
        return self.__name


class HersheyKisses(Weapon):

    def __init__(self):
        self.__name = 'Hershey Kisses'
        self.__attack = 1

    def attack(self):
        return self.__attack
    def get_name(self):
        return self.__name

class SourStraw(Weapon):

    def __init__(self):
        self.__name = 'Sour Straws'
        self.__attack = (random.randint(100,175))/100
        self.__stock = 6
        self.__max = 2
    def add_inv(self):
        if(self.__stock + 1 > self.__max):
            print("Cannot carry any more!")
        else:
           self.__stock = self.__stock + 1
    def get_name(self):
        return self.__name
    def attack(self):
        if(self.__stock > 0):
            self.__stock = self.__stock - 1
            return (random.randint(100,175))/100
        else:
            print("Stock is empty and you've missed a turn!")
            return 0


class ChocolateBars(Weapon):

    def __init__(self):
        self.__name = 'Chocolate Bars'
        self.__attack = (random.randint(200,240))/100
        self.__stock = 4
        self.__max = 4
    def add_inv(self):
        if(self.__stock + 1 > self.__max):
            print("Cannot carry any more!")
        else:
           self.__stock = self.__stock + 1
    def get_name(self):
        return self.__name
    def attack(self):
        if(self.__stock > 0):
            self.__stock = self.__stock - 1
            return (random.randint(200,240))/100
        else:
            print("Stock is empty and you've missed a turn!")
            return 0


class NerdBombs(Weapon):

    def __init__(self):
        self.__name = 'Nerd Bombs'
        self.__attack = (random.randint(350, 500))/100
        self.__stock = 1
        self.__max = 1
    def add_inv(self):
        if(self.__stock + 1 > self.__max):
            print("Cannot carry any more!")
        else:
           self.__stock = self.__stock + 1
    def get_name(self):
        return self.__name
    def attack(self):
        if(self.__stock > 0):
            self.__stock = self.__stock - 1
            return (random.randint(350, 500))/100
        else:
            print("Stock is empty and you've missed a turn!")
            return 0

#Player class to be controlled
class Player:

    def __init__(self):
        '''
        : Initializer for player
        '''
        self.__inventory = {1:HersheyKisses(), 2:SourStraw(), 3:ChocolateBars(),
        4:NerdBombs()}
        self.__attack = random.randint(10,20)
        self.__health = random.randint(100,120)

    def get_weapon(self,index):
        return self.__inventory[index]

    def get_attack(self):
        return random.randint(10,20)

    def get_health(self):
        return self.__health

    def set_health(self,health):
        self.__health = health

    def print_inventory(self):
        for i in range(1, len(self.__inventory) + 1):
            print(self.__inventory[i].get_name() + ", " + str(i))


# Houses contain monsters. The aim of the game is to eliminate all the monsters
# from the houses. This class observes the neighborhood to update it when an
# enemy has been defeated.
class House(Observer):

    #Container for the saved people
    __people = []
    #Container for the monsters
    __monsters = []
    #Dictionary to hold each type of NPC
    __monster_type = {1: Person(), 2: Zombie(), 3: Vampire(), 4: Ghoul(),
    5: Werewolf()}
    #The current amount of monsters in the house
    __monster_count = 0
    #The total number of monsters in the neighborhood
    __neighborhood_monsters = 0

    def __init__(self):
        '''
        : Initializer for the House
        '''
        self.__monster_count = random.randint(1,10)
        self.__monsters.append(self.__monster_type[random.randint(2, 5)])
        for i in range(0,self.__monster_count):
            self.__monsters.append(self.__monster_type[random.randint(2, 5)])

    def update(self):
        '''
        : Tells all the houses of the neighborhood an enemy has been defeated
        '''
        self.__neighborhood_monsters = self.__neighborhood_monsters - 1

    def item_drop(self,player):
        '''
        : Gives the player items from the People of the game
        :param player The player to give items to
        '''
        for i in range(0,len(self.__people)):
            self.__people[i].item_drop(player)

    def get_monster(self, index):
        return self.__monsters[index]

    def save_person(self,index):
        '''
        : Transforms a monster into a person
        :param index The index of the monster that has been returned to being a person:
        '''
        self.__monster_count = self.__monster_count-1
        self.__people.append(self.__monsters[index])

    def get_neighborhood_count(self):
        return self.__neighborhood_monsters

    def set_neighborhood_monsters(self, monsters):
        '''
        : Sets the current amount of monsters in the neighborhood
        :param monsters the amount of monsters in the neighborhood
        '''
        self.__neighborhood_monsters = monsters

    def get_monster_count(self):
        return self.__monster_count


def main():

    # Initializes world
    neighborhood = Neighborhood()
    # Initializes player
    player = Player()
    i = 0
    j = 0
    for i in range(len(neighborhood.grid)):
        for j in range(len(neighborhood.grid[0])):
            neighborhood.grid[i][j].set_neighborhood_monsters(neighborhood.get_monster_count())
    i = 0
    j = 0
    #Current monster
    k = 0
    #Current weapon
    l = 1
    while True:

        current_monster = None
        #The current house the player is in
        current_house =  neighborhood.get_current_house(i,j)
        # Checks if all enemies have been defeated
        if(current_house.get_neighborhood_count() <= 0):
            print("You win! You've saved the neighborhood!")
            time.sleep(5)
            sys.exit(0)
        #Sets current monster
        current_monster = current_house.get_monster(k)
        print("Now entering house number "+str(i+j+1))
        #Loops until house is cleared
        while (current_house.get_monster_count() > 0):
            print("You're currently facing a "+current_monster.get_name())
            print("Monster HP: "+str(current_monster.get_health())+" Your HP: "+
            str(player.get_health()))
            option = input("Attack or choose inventory?  ")
            if(option == 'attack'):
                attack = player.get_weapon(l).attack()*player.get_attack()
                health = current_monster.get_health()-attack
                current_monster.set_health(health)
                player.set_health(player.get_health()-current_monster.get_attack())
            else:
                player.print_inventory()
                cycle = 0
                try:
                    cycle = int(input("Chose the number of the weapon you want to equip:  "))
                except:
                    print("Input must be numeric from 1-5")
                    cycle = 1
                if(cycle < 1 or cycle > 5):
                    print("Invalid choice, attacking with Hershey Kisses.")
                    attack = player.get_weapon(l).attack()*player.get_attack()
                    health = current_monster.get_health()-attack
                    current_monster.set_health(health)
                    player.set_health(player.get_health()-current_monster.get_attack())
                else:
                    l = cycle
                    attack = player.get_weapon(l).attack()*player.get_attack()
                    health = current_monster.get_health()-attack
                    current_monster.set_health(health)
                    player.set_health(player.get_health()-current_monster.get_attack())

            if(player.get_health() <= 0):
                print("You've died! Game over!")
                time.sleep(5)
                sys.exit(0)
            if(current_monster.get_health() <= 0):
                neighborhood.update()
                current_house.save_person(k)
                k = k + 1
                current_monster= current_house.get_monster(k)
                health = current_monster.get_health()
            current_house.item_drop(player)
        i = i + 1
        if (current_house.get_neighborhood_count() <= 0):
            print("You win! You've saved the neighborhood!")
            time.sleep(5)
            sys.exit(0)
        k = 0
        if(i > 1):
            i = 0
            j = j + 1

main()
