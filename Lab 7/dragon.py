# Lab 7
# Kamal Ali & William Nguyen
# 10/8/2025
# a subclass of Entity superclass that has a basic attack and special attack

import random
from entity import Entity   # inherit from Entity

class Dragon(Entity):
    def basic_attack(self,hero):
        damage = random.randint(2,5)    # damage between 2 and 5
        hero.take_damage(damage)        # hero takes damage (from Entity)
        print(f"{self.name} smashes you with its tail for {damage} damage!")
    
    def special_attack(self,hero):
        damage = random.randint(3,7)    # damage between 3 and 7
        hero.take_damage(damage)        # apply damage
        print(f"{self.name} slashes you with its claws for {damage} damage!")
