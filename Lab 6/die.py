# Lab 6
# Kamal Ali & William Nguyen
# 9/29/2024
# Create a Die object that can roll a random number between 1 and 6

import random
class Die:
    def __init__(self, sides = 6):
        self._side = sides      # number of sides (used in roll())
        self._value = 0         # initialize value to 0
        self.roll()             # update self.value
    
    def roll(self):
        self._value = random.randint(1,self._side)  # set self._value to a random # between 1 and 6
        return self._value
    
    def __str__(self):
        return f"{self._value}"     # return die value as a string
    
    def __lt__(self, other):
        return self._value < other._value   # return true if value of self is less than other
    
    def __eq__(self, other):
        return self._value == other._value  # return true if value of self is equal to other
    
    def __sub__(self,other):
        return self._value - other._value   # return difference between value of self and value of ther
