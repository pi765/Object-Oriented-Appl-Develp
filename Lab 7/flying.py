# Lab 7
# Kamal Ali & William Nguyen
# 10/8/2025
# a subclass of Dragon superclass that overrides Dragon special attack with a swoop attack

import random
from dragon import Dragon   # inherit from Dragon

class FlyingDragon(Dragon):
    def __init__(self,name,hp):
        super().__init__(name,hp)       # call super to set name and hp
        self._swoops = 3                # default number of swoops
    
    def special_attack(self,hero):      # override special attack
        if self._swoops > 0:            # if there are swoops remaining
            damage = random.randint(5,8)        # damage between 5 and 8
            hero.take_damage(damage)            # apply damage
            self._swoops = self._swoops - 1     # reduce numnber of swoops remaining
            print(f"{self.name} swoops in and hits you for {damage} damage!")
        else:
            print(f"{self.name} tries an aerial attack but is all out of swoop attacks.")
        
    def __str__(self):
        return super().__str__() + f"\nSwoop attacks remaining: {self._swoops}" # gets __str__ from Entity class and concatenates number of swoops
