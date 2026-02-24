# Lab 9
# Kamal Ali & William Nguyen
# 10/20/2024
# A door that is either push or pull

import random
from door import Door

class BasicDoor(Door):  # inherit from Door class
    def __init__(self):
        self.unlocked = False  # door is locked
        self.state = random.randint(1,2) # 1 is push, 2 is pull
       
    def examine_door(self):
        return f"You encounter a basic door, you can either push it or pull it to open."    # string description of door
   
    def menu_options(self):
        return f"1. Push\n2. Pull"
   
    def get_menu_max(self):
        return 2            # 2 choices
   
    def attempt(self,option):
        if option == 1 and self.state == 1:     # if pushing the door was correct
            self.unlocked = True
            return f"You push the door."
        elif option == 1 and self.state == 2:   # push, but incorrect
            return f"You push the door."
        elif option == 2 and self.state == 2:   # if pulling the door was correct
            self.unlocked = True
            return f"You pull the door."
        else:                                   # pull, but incorrect
            return f"You pull the door."
       
    def is_unlocked(self):
        return self.unlocked    # True if True, False if False
       
    def clue(self):
       return f"Try the other way."
    
    def success(self):
        return f"Congratulations, you opened the door."