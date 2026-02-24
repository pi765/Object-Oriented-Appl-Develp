# Lab 10
# Kamal Ali & William Nguyen
# 10/30/2024
# Enemy class that can attack

from entity import Entity
import random

class Enemy(Entity):
    def __init__(self):
        monsters = ['Goblin', 'Vampire', 'Ghoul', 'Skeleton', 'Zombie']
        name = random.choice(monsters)  # random monster from the monsters list
        hp = random.randint(4,8)        # random hp
        super().__init__(name, max_hp=hp)   # initialize name and max_hp

    def attack(self,entity):
        dmg = random.randint(1,4)
        entity.take_damage(dmg)         # deal random damage to the entity
        return f"{self.name} attacks {entity.name} for {dmg} damage."   # string representing the attack