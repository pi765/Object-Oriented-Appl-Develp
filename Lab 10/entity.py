# Lab 10
# Kamal Ali & William Nguyen
# 10/30/2024
# Abstract Entity Class with a damage and heal function

import abc

class Entity(abc.ABC):
    def __init__(self,name,max_hp):
        self._name = name           # initialize name, hp, max_hp
        self._max_hp = max_hp
        self._hp = max_hp

    @property           # getters
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    def take_damage(self,dmg):
        self._hp = self._hp - dmg   # reduce hp by dmg
        if self._hp < 0:
            self._hp = 0            # health can't drop below 0

    def heal(self):
        self._hp = self._max_hp     # set hp to full
    
    def __str__(self):
        return f"{self._name}\nHP: {self._hp}/{self._max_hp}"   # return a string for the name of the entity and their hp
    
    @abc.abstractmethod
    def attack(self,entity):    # abstract method, overridden by hero and enemy
        pass