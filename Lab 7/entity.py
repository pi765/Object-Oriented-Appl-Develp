# Lab 7
# Kamal Ali & William Nguyen
# 10/8/2025
# Create the entity class which stores name and hp, applies damage, and prints the name/hp

class Entity:
    def __init__(self,name,max_hp):     # initialize variables
        self._name = name               # name
        self._max_hp = max_hp           # max hp
        self._hp = max_hp               # hp = max hp

    @property       # getter decorator
    def name(self):
        return self._name   # return the name
    
    @property       # getter decorator
    def hp(self):
        return self._hp     # return current hp
    
    def take_damage(self,dmg):
        self._hp = self._hp - dmg   # reduce hp by dmg
        if self._hp < 0:
            self._hp = 0            # health can't drop below 0
        
    def __str__(self):
        return f"{self._name}: {self._hp}/{self._max_hp}"   # return string in format "name: hp/max_hp"