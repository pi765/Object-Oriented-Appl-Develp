# Lab 7
# Kamal Ali & William Nguyen
# 10/8/2025
# a subclass of Entity superclass that has a sword attack and arrow attack

import random
from entity import Entity   # inherit from Entity

class Hero(Entity):
    def sword_attack(self,dragon):
        damage = random.randint(1,6) + random.randint(1,6) # damage is 2 rolls between 1 and 6
        dragon.take_damage(damage)                         # apply damage to the dragon (take_damage from Entity class)
        print(f"You slash the {dragon.name} with your sword for {damage} damage.")
    
    def arrow_attack(self,dragon):
        damage = random.randint(1,12)   # 1 roll between 1 and 12
        dragon.take_damage(damage)      # apply damage
        print(f"You hit the {dragon.name} with an arrow for {damage} damage.")