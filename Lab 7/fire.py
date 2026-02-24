# Lab 7
# Kamal Ali & William Nguyen
# 10/8/2025
# a subclass of Dragon superclass that overrides the regular Dragon special attack with a fire shot

import random
from dragon import Dragon   # inherit from Dragon

class FireDragon(Dragon):
    def __init__(self, name, hp):
        super().__init__(name,hp)   # set name and hp
        self.fire_shots = 2         # default number of fire shots

    def special_attack(self, hero):     # override special attack
        if self.fire_shots > 0:
            damage = random.randint(6,9)    # if there are any fire shots, deal damage between 6-9
            hero.take_damage(damage)        # apply damage
            self.fire_shots = self.fire_shots - 1   # reduce the number of fire shots remaining
            print(f"{self.name} engulfs you in flames for {damage} damage!")
        else:
            print(f"{self.name} tries to spit fire at you but is all out of fire shots.")
        
    def __str__(self):
        return super().__str__() + f"\nFire Shots remaining: {self.fire_shots}"
