# Lab 10
# Kamal Ali & William Nguyen
# 10/30/2024
# Hero class, the player, can attack and move in 4 directions

from entity import Entity
from map import Map
import random

class Hero(Entity):
    def __init__(self,name):
        super().__init__(name, max_hp=25)   # initialize name and max_hp
        self._loc = [0,0]   # [n/s, w/e]

    @property   # get property for location
    def loc(self):
        return self._loc

    def attack(self,entity):
        dmg = random.randint(2,5)
        entity.take_damage(dmg)     # deal random damage between 2-5
        return f"{self.name} attacks a {entity.name} for {dmg} damage."     # return string
    
    def go_north(self):
        updated_loc = self._loc[0] - 1
        map = Map()
        if updated_loc >= 0 and updated_loc <= len(map)-1:      # check to see if movement is in bounds
            self._loc[0] -= 1                                   # update position
            return map[self._loc[0]][self._loc[1]]              # return the char at the map location
        else:
            return 'o'  # don't move, return 'o'
        
    def go_south(self):
        updated_loc = self._loc[0] + 1
        map = Map()
        if updated_loc >= 0 and updated_loc <= len(map)-1:
            self._loc[0] += 1
            return map[self._loc[0]][self._loc[1]]
        else:
            return 'o'
        
    def go_east(self):
        updated_loc = self._loc[1] + 1
        map = Map()
        if updated_loc >= 0 and updated_loc <= len(map)-1:
            self._loc[1] += 1
            return map[self._loc[0]][self._loc[1]]
        else:
            return 'o'

    def go_west(self):
        updated_loc = self._loc[1] - 1
        map = Map()
        if updated_loc >= 0 and updated_loc <= len(map)-1:
            self._loc[1] -= 1
            return map[self._loc[0]][self._loc[1]]
        else:
            return 'o'