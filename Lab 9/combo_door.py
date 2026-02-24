# Lab 9
# Kamal Ali & William Nguyen
# 10/20/2024
# A combination door with 10 possible values

import random
from door import Door

class ComboDoor(Door):  # inherit from Door class
    def __init__(self):
        self.unlocked = False  # door is locked
        self.combination = random.randint(1,10) # 10 possible values
        self.higher = False  # if the value guessed was too high
       
    def examine_door(self):
        return f"You encounter a door with a combination lock. You can spin the dial to a number 1-10."
   
    def menu_options(self):
        return f"Enter # 1-10: "
   
    def get_menu_max(self):
        return 10            # number of values
   
    def attempt(self,option):
        if option == self.combination:
            self.unlocked = True
            return f"You turn the dial to... {option}"
        elif option > self.combination:
            self.higher = True      # too high
            return f"You turn the dial to... {option}"
        else:
            self.higher = False     # too low
            return f"You turn the dial to... {option}"
       
    def is_unlocked(self):
        return self.unlocked    # True if True, False if False
       
    def clue(self):
       if self.higher == True:                      # if option in attempt(self,option) is higher than the combination
           return f"Too high. Try a lower value."
       else:
           return f"Too low. Try a higher value."
    
    def success(self):
        return f"You found the correct value and opened the door."