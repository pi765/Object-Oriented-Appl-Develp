# Lab 9
# Kamal Ali & William Nguyen
# 10/20/2024
# A locked door with a key hidden in 3 locations

import random
from door import Door

class LockedDoor(Door):  # inherit from Door class
    def __init__(self):
        self.unlocked = False  # door is locked
        self.location = random.randint(1,3) # 1 is mat, 2 is flower pot, 3 is rock
       
    def examine_door(self):
        return f"You encounter a locked door. The key is hidden nearby. Look around for the key."
   
    def menu_options(self):
        return f"1. Look under the mat.\n2. Look under the flower pot.\n3. Look under the fake rock."
   
    def get_menu_max(self):
        return 3            # number of locations
   
    def attempt(self,option):
        if option == 1:                             # user chose mat
            if self.location == 1:                  # correct location
                self.unlocked = True
                return f"You look under the mat."
            else:                                   # incorrect location
                return f"You look under the mat."
        elif option == 2:                           # pot
            if self.location == 2:
                self.unlocked = True
                return f"You look under the flower pot."
            else:
                return f"You look under the flower pot."
        else:                                       # rock
            if self.location == 3:
                self.unlocked = True
                return f"You look under the fake rock."
            else:
                return f"You look under the fake rock."
       
    def is_unlocked(self):
        return self.unlocked    # True if True, False if False
       
    def clue(self):
       return f"Look somewhere else."
    
    def success(self):
        return f"You found the key and opened the door."